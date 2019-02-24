from flask import Flask, request, render_template, redirect, flash, url_for
import os, shutil
from re import sub
from git import Repo


app = Flask(__name__)
app.config['SECRET_KEY'] = "sdjkhgekjrhgjvshjkhsv"


def pretty_dir(dir):
	if '/' in dir:
		return dir.replace('/', '^')
	else:
		return dir


@app.route('/')
def index():
	return render_template('index.html')



@app.route('/clone', methods = ['GET', 'POST'])
def clone():
	if request.method == 'POST':
		url = request.form['url']
		dir_name = sub( '.git', '', url.split('/')[-1] )
		dir_to_clone = os.getcwd() + '/Repositories/' + dir_name
		if os.path.exists(dir_to_clone):
			flash('already')
			return redirect( url_for('clone') )
		try:
			repository = Repo.clone_from(url, dir_to_clone)
			repository.remotes.origin.fetch()
			repository.remotes.origin.pull()
			flash('success')
			return redirect(url_for('repositories'))
		except Exception:
			flash('notfound')
			return redirect( url_for('clone') )
	return render_template('clone.html')


@app.route('/repositories')
def repositories():
	reps_dir = os.getcwd() + '/Repositories'
	reps = os.listdir(reps_dir)
	return render_template('repositories.html', reps = reps)

@app.route('/repositories/<rep_name>', methods = ['GET', 'POST'])
def repository(rep_name):
	reps_dir = os.getcwd() + '/Repositories/'
	repository = Repo(reps_dir + rep_name)
	return render_template('repository.html', rep = repository, name = rep_name, pretty = pretty_dir)

@app.route('/repositories/delete/<rep_name>')
def del_repository(rep_name):
	reps_dir = os.getcwd() + '/Repositories/'
	repository = reps_dir + rep_name

	if not os.path.exists(repository):
		flash('notfound')
		return redirect( url_for('repositories') )
	shutil.rmtree(repository)
	flash('success')
	return redirect(url_for('repositories'))


@app.route('/repositories/branch/add', methods = ['GET', 'POST'])
def add_branch():
	reps_dir = os.getcwd() + '/Repositories/'
	if request.method == 'POST':
		branch_name = request.form['branchName'].replace(' ', '')
		rep_name = request.form['repositoryName']
		repository = Repo(reps_dir + rep_name)
		if branch_name not in repository.branches and 'origin/'+branch_name not in [name.name for name in repository.remotes.origin.refs]:
			repository.create_head(branch_name).checkout()
			return redirect(url_for('repository', rep_name=rep_name))
		flash('branch_exists')
		return redirect(url_for('repository', rep_name=rep_name))

@app.route('/repositories/branch/delete/<rep_name>/<branch_name>', methods = ['GET', 'POST'])
def del_branch(rep_name, branch_name):
	reps_dir = os.getcwd() + '/Repositories/'
	if request.method == 'GET':
		repository = Repo(reps_dir + rep_name)
		if branch_name in repository.branches and branch_name not in repository.remotes.origin.refs:
			repository.delete_head(branch_name)
			return redirect(url_for('repository', rep_name=rep_name))
		elif branch_name in repository.remotes.origin.refs:
			repository.delete_head('-D', branch_name)
			return redirect(url_for('repository', rep_name=rep_name))
		return redirect(url_for('repository', rep_name=rep_name))

@app.route('/repositories/branch/switch/<rep_name>/<branch_name>', methods = ['GET', 'POST'])
def switch_branch(rep_name, branch_name):
	reps_dir = os.getcwd() + '/Repositories/'
	if request.method == 'GET':
		repository = Repo(reps_dir + rep_name)
		if branch_name in repository.branches:
			repository.git.checkout(branch_name)
			return redirect(url_for('repository', rep_name=rep_name))
		elif branch_name in repository.remotes.origin.refs:
			branch_index = [name.name for name in repository.remotes.origin.refs].index(f'origin/{branch_name}')
			remote_branch = repository.remotes.origin.refs[branch_index]
			fetched_branch = repository.create_head(branch_name, remote_branch).checkout()
			# repository.remotes.origin.pull()
			return redirect(url_for('repository', rep_name=rep_name))
		return redirect(url_for('repository', rep_name=rep_name))



@app.route('/repositories/add/<rep_name>/<file_name>', methods = ['GET', 'POST'])
def add_file(file_name, rep_name):
	reps_dir = os.getcwd() + '/Repositories/'
	if request.method == 'GET':
		repository = Repo(reps_dir + rep_name)
		if '^' in file_name:
			file_name = file_name.replace('^', '/')
			repository.index.add([file_name])
			return redirect(url_for('repository', rep_name=rep_name))
		repository.index.add([file_name])
		return redirect(url_for('repository', rep_name=rep_name))

@app.route('/repositories/add/all/<rep_name>', methods = ['GET', 'POST'])
def add_all_files(rep_name):
	reps_dir = os.getcwd() + '/Repositories/'
	if request.method == 'GET':
		repository = Repo(reps_dir + rep_name)
		if len(repository.untracked_files) + len(repository.index.diff(None)) == 0:
			return redirect(url_for('repository', rep_name=rep_name))
		repository.git.add('--all')
		return redirect(url_for('repository', rep_name=rep_name))


@app.route('/repositories/reset/<rep_name>/<file_name>', methods = ['GET', 'POST'])
def reset_file(file_name, rep_name):
	reps_dir = os.getcwd() + '/Repositories/'
	if request.method == 'GET':
		repository = Repo(reps_dir + rep_name)
		if '^' in file_name:
			file_name = file_name.replace('^', '/')
			try:
				repository.index.remove([file_name])

			except Exception:
				flash('staged')
				return redirect(url_for('repository', rep_name=rep_name))

		try:
			repository.index.remove([file_name])
		except Exception:
			return redirect(url_for('repository', rep_name=rep_name))
		return redirect(url_for('repository', rep_name=rep_name))


@app.route('/repositories/commit', methods = ['GET', 'POST'])
def commit():
	reps_dir = os.getcwd() + '/Repositories/'
	if request.method == 'POST':
		rep_name = request.form['repositoryName']
		message = request.form['message'] if request.form['message'] else 'new commit'
		repository = Repo(reps_dir + rep_name)
		if len(repository.index.diff(repository.head.commit)) == 0:
			flash('nothing')
			return redirect(url_for('repository', rep_name=rep_name))
		repository.git.commit(m=message)
		flash('commited')
		return redirect(url_for('repository', rep_name=rep_name))

@app.route('/repositories/push/<rep_name>', methods = ['GET', 'POST'])
def push(rep_name):
	reps_dir = os.getcwd() + '/Repositories/'
	repository = Repo(reps_dir + rep_name)
	branch = repository.active_branch
	repository.git.push('origin', branch)
	flash('pushed')
	return redirect(url_for('repository', rep_name=rep_name))



if __name__ == '__main__':
	app.run(debug=True)
