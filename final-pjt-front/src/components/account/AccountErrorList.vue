<template>
  <div class="account-error-list">
    <div v-for="(errors, field) in authError" :key="field">
      <!-- {{ field }} -->
      <div>
        <div v-for="(error, idx) in errors" :key="idx">
          <!-- {{ error }} -->
          <div id="debug" v-if="error" class="text-center mb-3">입력 정보가 불확실합니다.</div>
          <div v-else></div>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
  import { mapGetters } from 'vuex'
  
  export default {
    name: 'AccountErrorList',
    computed: {
      ...mapGetters(['authError'])
    },
    mounted() {
      setTimeout(() => { location.reload() }, 2000)
    },
  }
</script>

<style>

  @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100;300;400;500;700;900&display=swap');

  #debug {
    font-family: 'Noto Sans KR',  sans-serif;
    font-weight: 500;
    font-size: 18px;
    color: #ff0053;
  }
</style>
