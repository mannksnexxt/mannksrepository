const isEmpty = function(value) {
    if (value !== '' && value !== null && value !== '?') {
        return false;
    }
    return true;
}
const fromDegrees = (string) => {
    numbers = string.split('°');
    if (string[0] === '-') return +numbers[0] - parseFloat(numbers[1]) / 60;
    else return +numbers[0] + parseFloat(numbers[1]) / 60;
}
const toDegrees = (number) => {
    degree = number.toString().split('.')[0] + '° ';
    minutes = ( (number - Math.floor(number)) * 60).toFixed(1);
    return degree + minutes.toString();
}
const toRadians = (number) => {
    return (number * Math.PI) / 180;
}


let vm = new Vue({
    el: '#app',
    data: {
        headData: {
            i: localStorage.getItem('i'),
            H: localStorage.getItem('H'),
            zeroPlace: localStorage.getItem('zero')
        },
        mainData: {
            horizontalCircle: null,
            verticalCircle: null,
            distance: null,
            U: null
        },
        menu: false
    },
    methods: {
        closeMenu: function() {
            if (this.menu == true) this.menu = false;
        },
        fixValues: function() {
            localStorage.setItem('i', this.headData.i);
            localStorage.setItem('H', this.headData.H);
            localStorage.setItem('zero', this.headData.zeroPlace);
            swal({
                title: "Значения изменены!",
                icon: "success",
                button: "Ok"
            });
        },
        clearValues: function() {
            for (key in this.mainData) {
                this.mainData[key] = null;
            }
            swal({
                title: "Поля очищены!",
                icon: "success",
                button: "Ok"
            });
        }
    },
    computed: {
        computeV: function() {
            if (!isEmpty(this.headData.zeroPlace) && !isEmpty(this.mainData.verticalCircle)) {
                result = fromDegrees(this.mainData.verticalCircle) - fromDegrees(this.headData.zeroPlace);
                return toDegrees(result);
            }
            return '?'
        },
        computeS: function() {
            if (!isEmpty(this.computeV) && !isEmpty(this.mainData.distance)) {
                return (+this.mainData.distance * Math.pow( Math.cos(toRadians(fromDegrees(this.computeV))), 2)).toFixed(4);
            }
            return '?'
        },
        computeHi: function() {
            if (!isEmpty(this.computeV) && !isEmpty(this.computeS)) {
                return (Math.tan(toRadians(fromDegrees(this.computeV))) * this.computeS).toFixed(2);
            }
            return '?';

        },
        computeD: function() {
            if (!isEmpty(this.headData.i) && !isEmpty(this.mainData.U)) {
                return (+this.headData.i - +this.mainData.U).toFixed(2);
            }
            return '?';
        },
        computeH: function() {
            if (!isEmpty(this.computeHi) && !isEmpty(this.computeD)) {
                return (parseFloat(this.computeHi) + parseFloat(this.computeD)).toFixed(2);
            }
            return '?';
        },
        computeGlobalH: function() {
            if (!isEmpty(this.headData.H) && !isEmpty(this.computeH)) {
                return (parseFloat(this.headData.H) + parseFloat(this.computeH)).toFixed(2);
            }
            return '?';
        }
    }
})
Vue.config.devtools = true;
