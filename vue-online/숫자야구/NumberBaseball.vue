<template>
    <div>
        <h1>{{result}}</h1>
        <form @submit.prevent="onSubmitForm"><!--v-on: = @ 로 대체 가능 //  e.preventDefault(); = submit.prevent 대체가능 -->
            <input ref="answer" maxlength="4" v-model="value"/>
            <button type="submit">입력</button>
        </form>
        <div>시도 : {{tries.length}}</div>
        <ul>
            <li v-for="t in tries">
                <div>{{t.try}}</div>
                <div>{{t.result}}</div>
            </li>
        </ul>
    </div>
</template>

<script>
    export default{
        data(){
            return{
                answer:getNumbers(),
                tries:[],
                value:'',
                result:'',
            }
        },
        methods:{
            onSubmitForm(){
                this.tries.push({
                    try:this.value,
                    result:'홈런',
                });
                this.value = '';
                this.$refs.answer.focus();
            }
        }
    };
</script>

<style></style>