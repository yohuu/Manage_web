<template>
  <div id="app">
    <el-row type="flex" class="row-bg" justify="center" align="middle">
      <el-col :span="6">
        <div class="grid-content">
          <div>
          </div>
        </div>
      </el-col>

      <el-col :span="6">
        <el-popover
          ref="popover"
          placement="left"
          width="10"
          trigger="hover"
          popper-class="dio">
            <el-button type="text">{{ state }}</el-button>
        </el-popover>
        <div class="grid-content test"  v-popover:popover>
          <div>
            <img src="./assets/photo.png">
          </div>
        </div>
      </el-col>

      <el-col :span="6" >
        <div class="grid-content">
          <span id='name'>{{ name }}</span>
          <span id='sentence'>{{ sentence }}</span>
        </div>
      </el-col>
    </el-row>
    <hr/>
    <router-view/>
  </div>

</template>

<script>
export default {
  name: 'App',
  data () {
    return {
      state: '登录',
      name: '郑鹏威',
      sentence: '你说情到深处人怎能不孤独 , 爱到浓时就牵肠挂肚'
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 20px;
  min-width: 1500px;
}
.dio {
  text-align: center;
}
.el-col {
  width: 100px;
  height: 100px;
  font-size: 70%;
  margin-left: 50px;
  border-radius: 50%;
  overflow-x: hidden;
}
.el-col:nth-child(3) {
  width: 800px;
  border-radius: 10px;
  line-height: 100px;
}
.test {
  position: relative;
  width: 100%;
  height: 100%;
  background-color: #aaaaaa;
}
.grid-content img {
  width: 100%;
  height: 100%;
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
}
#sentence {
  padding-left: 200px;
}
</style>
