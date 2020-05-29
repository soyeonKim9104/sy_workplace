//vue 환경에서는 외부 경로를 import...from으로 불러옴

import Vue from 'vue';

import NumberBaseball from './NumberBaseball';

new Vue(NumberBaseball).$mount('#root');