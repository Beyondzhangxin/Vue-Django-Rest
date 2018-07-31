<template>
    <div class="analysis">
        <el-header id="header">
            <el-row>
                <el-col :span="3"><div class="grid-content">
                    <el-button id="button">
                        <img src="../../assets/station.png" id="image">
                        <span id="text">电站对比</span>
                    </el-button>
                </div></el-col>
                <el-col :span="3"><div class="grid-content">
                    <el-button id="button">
                        <img src="../../assets/self.png" id="image">
                        <span id="text">设备对比</span>
                    </el-button>
                </div></el-col>
                <el-col :span="3"><div class="grid-content">
                    <el-button id="button">
                        <img src="../../assets/equipment.png" id="image">
                        <span id="text">自身对比</span>
                    </el-button>
                </div></el-col>
                <el-col :span="3"><div class="grid-content"></div></el-col>
            </el-row>
        </el-header>


        <el-main>



        </el-main>

        <el-main>



        </el-main>

        <el-main>



        </el-main>
        </div>
</template>



<script>
export default {
    
}
</script>


<style>
#header{
    background:white;
    height:100px;
}

#button{
    /* margin-top:8px; */
}

#text{
   padding-bottom:2px;
   display: block;
}
</style>
