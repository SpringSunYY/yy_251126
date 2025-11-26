<template>
  <div class="app-container">
    <el-form :model="queryParams" ref="queryForm" size="small" :inline="true" v-show="showSearch" label-width="68px">
      <el-form-item label="编号" prop="recruitId">
        <el-input
          v-model="queryParams.recruitId"
          placeholder="请输入编号"
          clearable
          @keyup.enter.native="handleQuery"
        />
      </el-form-item>
      <el-form-item label="岗位" prop="post">
        <el-input
          v-model="queryParams.post"
          placeholder="请输入岗位"
          clearable
          @keyup.enter.native="handleQuery"
        />
      </el-form-item>
      <el-form-item label="地点" prop="location">
        <el-input
          v-model="queryParams.location"
          placeholder="请输入地点"
          clearable
          @keyup.enter.native="handleQuery"
        />
      </el-form-item>
      <el-form-item label="经验要求" prop="experienceRequired">
        <el-select v-model="queryParams.experienceRequired" placeholder="请选择经验要求" clearable>
          <el-option
            v-for="dict in dict.type.recruit_experience_required"
            :key="dict.value"
            :label="dict.label"
            :value="dict.value"
          />
        </el-select>
      </el-form-item>
      <el-form-item label="学历要求" prop="educationRequired">
        <el-select v-model="queryParams.educationRequired" placeholder="请选择学历要求" clearable>
          <el-option
            v-for="dict in dict.type.recruit_education_required"
            :key="dict.value"
            :label="dict.label"
            :value="dict.value"
          />
        </el-select>
      </el-form-item>
      <el-form-item label="技能要求" prop="skillRequired">
        <el-input
          v-model="queryParams.skillRequired"
          placeholder="请输入技能要求"
          clearable
          @keyup.enter.native="handleQuery"
        />
      </el-form-item>
      <el-form-item label="企业名称" prop="enterpriseName">
        <el-input
          v-model="queryParams.enterpriseName"
          placeholder="请输入企业名称"
          clearable
          @keyup.enter.native="handleQuery"
        />
      </el-form-item>
      <el-form-item label="上市情况" prop="listingStatus">
        <el-select v-model="queryParams.listingStatus" placeholder="请选择上市情况" clearable>
          <el-option
            v-for="dict in dict.type.recruit_listing_status"
            :key="dict.value"
            :label="dict.label"
            :value="dict.value"
          />
        </el-select>
      </el-form-item>
      <el-form-item label="企业规模" prop="enterpriseSize">
        <el-select v-model="queryParams.enterpriseSize" placeholder="请选择企业规模" clearable>
          <el-option
            v-for="dict in dict.type.recruit_enterprise_size"
            :key="dict.value"
            :label="dict.label"
            :value="dict.value"
          />
        </el-select>
      </el-form-item>
      <el-form-item label="主营业务" prop="mainBusiness">
        <el-input
          v-model="queryParams.mainBusiness"
          placeholder="请输入主营业务"
          clearable
          @keyup.enter.native="handleQuery"
        />
      </el-form-item>
      <el-form-item label="标题详情" prop="titleDetail">
        <el-input
          v-model="queryParams.titleDetail"
          placeholder="请输入标题详情"
          clearable
          @keyup.enter.native="handleQuery"
        />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" icon="el-icon-search" size="mini" @click="handleQuery">搜索</el-button>
        <el-button icon="el-icon-refresh" size="mini" @click="resetQuery">重置</el-button>
      </el-form-item>
    </el-form>

    <el-row :gutter="10" class="mb8">
      <el-col :span="1.5">
        <el-button
          type="primary"
          plain
          icon="el-icon-plus"
          size="mini"
          @click="handleAdd"
          v-hasPermi="['recruit:recruit:add']"
        >新增</el-button>
      </el-col>
      <el-col :span="1.5">
        <el-button
          type="success"
          plain
          icon="el-icon-edit"
          size="mini"
          :disabled="single"
          @click="handleUpdate"
          v-hasPermi="['recruit:recruit:edit']"
        >修改</el-button>
      </el-col>
      <el-col :span="1.5">
        <el-button
          type="danger"
          plain
          icon="el-icon-delete"
          size="mini"
          :disabled="multiple"
          @click="handleDelete"
          v-hasPermi="['recruit:recruit:remove']"
        >删除</el-button>
      </el-col>
      <el-col :span="1.5">
        <el-button
          type="warning"
          plain
          icon="el-icon-download"
          size="mini"
          @click="handleExport"
          v-hasPermi="['recruit:recruit:export']"
        >导出</el-button>
      </el-col>
      <el-col :span="1.5">
        <el-button
          type="info"
          plain
          icon="el-icon-upload2"
          size="mini"
          @click="handleImport"
          v-hasPermi="['recruit:recruit:import']"
        >导入</el-button>
      </el-col>
      <right-toolbar :showSearch.sync="showSearch" @queryTable="getList" :columns="columns"></right-toolbar>
    </el-row>

    <el-table :loading="loading" :data="recruitList" @selection-change="handleSelectionChange">
      <el-table-column type="selection" width="55" align="center" />
      <el-table-column label="编号" align="center" v-if="columns[0].visible" prop="recruitId" />
      <el-table-column label="岗位" align="center" :show-overflow-tooltip="true" v-if="columns[1].visible" prop="post" />
      <el-table-column label="标题链接" align="center" :show-overflow-tooltip="true" v-if="columns[2].visible" prop="titleUrl" >
        <template slot-scope="scope">
          <a v-if="scope.row.titleUrl" :href="scope.row.titleUrl" target="_blank">查看</a>
        </template>
      </el-table-column>
      <el-table-column label="薪资范围" align="center" :show-overflow-tooltip="true" v-if="columns[3].visible" prop="salaryRange" />
      <el-table-column label="月薪最小值" align="center" :show-overflow-tooltip="true" v-if="columns[4].visible" prop="salaryMonthMin" />
      <el-table-column label="月薪最大值" align="center" :show-overflow-tooltip="true" v-if="columns[5].visible" prop="salaryMonthMax" />
      <el-table-column label="月薪平均值" align="center" :show-overflow-tooltip="true" v-if="columns[6].visible" prop="salaryMonthAvg" />
      <el-table-column label="地点" align="center" :show-overflow-tooltip="true" v-if="columns[7].visible" prop="location" />
      <el-table-column label="经验要求" align="center" v-if="columns[8].visible" prop="experienceRequired">
        <template slot-scope="scope">
          <dict-tag :options="dict.type.recruit_experience_required" :value="scope.row.experienceRequired"/>
        </template>
      </el-table-column>
      <el-table-column label="学历要求" align="center" v-if="columns[9].visible" prop="educationRequired">
        <template slot-scope="scope">
          <dict-tag :options="dict.type.recruit_education_required" :value="scope.row.educationRequired"/>
        </template>
      </el-table-column>
      <el-table-column label="技能要求" align="center" :show-overflow-tooltip="true" v-if="columns[10].visible" prop="skillRequired" />
      <el-table-column label="企业名称" align="center" :show-overflow-tooltip="true" v-if="columns[11].visible" prop="enterpriseName" />
      <el-table-column label="上市情况" align="center" v-if="columns[12].visible" prop="listingStatus">
        <template slot-scope="scope">
          <dict-tag :options="dict.type.recruit_listing_status" :value="scope.row.listingStatus"/>
        </template>
      </el-table-column>
      <el-table-column label="企业规模" align="center" v-if="columns[13].visible" prop="enterpriseSize">
        <template slot-scope="scope">
          <dict-tag :options="dict.type.recruit_enterprise_size" :value="scope.row.enterpriseSize"/>
        </template>
      </el-table-column>
      <el-table-column label="主营业务" align="center" :show-overflow-tooltip="true" v-if="columns[14].visible" prop="mainBusiness" />
      <el-table-column label="标题详情" align="center" :show-overflow-tooltip="true" v-if="columns[15].visible" prop="titleDetail" />
      <el-table-column label="薪资范围2" align="center" :show-overflow-tooltip="true" v-if="columns[16].visible" prop="salaryRange2" />
      <el-table-column label="岗位描述" align="center" :show-overflow-tooltip="true" v-if="columns[17].visible" prop="jobDescription" />
      <el-table-column label="工作地点" align="center" :show-overflow-tooltip="true" v-if="columns[18].visible" prop="wordLocation" />
      <el-table-column label="操作" align="center" class-name="small-padding fixed-width">
        <template slot-scope="scope">
          <el-button
            size="mini"
            type="text"
            icon="el-icon-edit"
            @click="handleUpdate(scope.row)"
            v-hasPermi="['recruit:recruit:edit']"
          >修改</el-button>
          <el-button
            size="mini"
            type="text"
            icon="el-icon-delete"
            @click="handleDelete(scope.row)"
            v-hasPermi="['recruit:recruit:remove']"
          >删除</el-button>
        </template>
      </el-table-column>
    </el-table>

    <pagination
      v-show="total>0"
      :total="total"
      :page.sync="queryParams.pageNum"
      :limit.sync="queryParams.pageSize"
      @pagination="getList"
    />

    <!-- 添加或修改招聘信息表对话框 -->
    <el-dialog :title="title" :visible.sync="open" width="500px" append-to-body>
      <el-form ref="form" :model="form" :rules="rules" label-width="80px">
        <el-form-item label="岗位" prop="post">
          <el-input v-model="form.post" placeholder="请输入岗位" />
        </el-form-item>
<!--        <el-form-item label="标题链接" prop="titleUrl">-->
<!--          <el-input v-model="form.titleUrl" placeholder="请输入标题链接" />-->
<!--        </el-form-item>-->
        <el-form-item label="薪资范围" prop="salaryRange">
          <el-input v-model="form.salaryRange" placeholder="请输入薪资范围" />
        </el-form-item>
<!--        <el-form-item label="月薪最小值" prop="salaryMonthMin">-->
<!--          <el-input v-model="form.salaryMonthMin" placeholder="请输入月薪最小值" />-->
<!--        </el-form-item>-->
<!--        <el-form-item label="月薪最大值" prop="salaryMonthMax">-->
<!--          <el-input v-model="form.salaryMonthMax" placeholder="请输入月薪最大值" />-->
<!--        </el-form-item>-->
<!--        <el-form-item label="月薪平均值" prop="salaryMonthAvg">-->
<!--          <el-input v-model="form.salaryMonthAvg" placeholder="请输入月薪平均值" />-->
<!--        </el-form-item>-->
        <el-form-item label="地点" prop="location">
          <el-input v-model="form.location" placeholder="请输入地点" />
        </el-form-item>
        <el-form-item label="经验要求" prop="experienceRequired">
          <el-select v-model="form.experienceRequired" placeholder="请选择经验要求">
            <el-option
              v-for="dict in dict.type.recruit_experience_required"
              :key="dict.value"
              :label="dict.label"
              :value="dict.value"
            ></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="学历要求" prop="educationRequired">
          <el-select v-model="form.educationRequired" placeholder="请选择学历要求">
            <el-option
              v-for="dict in dict.type.recruit_education_required"
              :key="dict.value"
              :label="dict.label"
              :value="dict.value"
            ></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="技能要求" prop="skillRequired">
          <el-input v-model="form.skillRequired" placeholder="请输入技能要求" />
        </el-form-item>
        <el-form-item label="企业名称" prop="enterpriseName">
          <el-input v-model="form.enterpriseName" placeholder="请输入企业名称" />
        </el-form-item>
        <el-form-item label="上市情况" prop="listingStatus">
          <el-select v-model="form.listingStatus" placeholder="请选择上市情况">
            <el-option
              v-for="dict in dict.type.recruit_listing_status"
              :key="dict.value"
              :label="dict.label"
              :value="dict.value"
            ></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="企业规模" prop="enterpriseSize">
          <el-select v-model="form.enterpriseSize" placeholder="请选择企业规模">
            <el-option
              v-for="dict in dict.type.recruit_enterprise_size"
              :key="dict.value"
              :label="dict.label"
              :value="dict.value"
            ></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="主营业务" prop="mainBusiness">
          <el-input v-model="form.mainBusiness" placeholder="请输入主营业务" />
        </el-form-item>
        <el-form-item label="标题详情" prop="titleDetail">
          <el-input v-model="form.titleDetail" placeholder="请输入标题详情" />
        </el-form-item>
        <el-form-item label="薪资范围2" prop="salaryRange2">
          <el-input v-model="form.salaryRange2" placeholder="请输入薪资范围2" />
        </el-form-item>
        <el-form-item label="岗位描述" prop="jobDescription">
          <el-input v-model="form.jobDescription" placeholder="请输入岗位描述" />
        </el-form-item>
        <el-form-item label="工作地点" prop="wordLocation">
          <el-input v-model="form.wordLocation" placeholder="请输入工作地点" />
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button type="primary" @click="submitForm">确 定</el-button>
        <el-button @click="cancel">取 消</el-button>
      </div>
    </el-dialog>

    <!-- 导入对话框 -->
    <el-dialog :title="upload.title" :visible.sync="upload.open" width="400px" append-to-body>
      <el-upload
        ref="upload"
        :limit="1"
        accept=".xlsx, .xls"
        :headers="upload.headers"
        :action="upload.url + '?updateSupport=' + upload.updateSupport"
        :disabled="upload.isUploading"
        :on-progress="handleFileUploadProgress"
        :on-success="handleFileSuccess"
        :auto-upload="false"
        drag
      >
        <i class="el-icon-upload"></i>
        <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
        <div class="el-upload__tip text-center" slot="tip">
          <div class="el-upload__tip" slot="tip">
            <el-checkbox v-model="upload.updateSupport" /> 是否更新已经存在的招聘信息表数据
          </div>
          <span>仅允许导入xls、xlsx格式文件。</span>
          <el-link type="primary" :underline="false" style="font-size:12px;vertical-align: baseline;" @click="importTemplate">下载模板</el-link>
        </div>
      </el-upload>
      <div slot="footer" class="dialog-footer">
        <el-button type="primary" @click="submitFileForm">确 定</el-button>
        <el-button @click="upload.open = false">取 消</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>


import { listRecruitInfo, getRecruitInfo, delRecruitInfo, addRecruitInfo, updateRecruitInfo } from "@/api/recruit/recruit";
import { getToken } from "@/utils/auth";

export default {
  name: "recruit_info",
  dicts: ['recruit_experience_required', 'recruit_education_required', 'recruit_listing_status', 'recruit_enterprise_size'],
  data() {
    return {
      // 遮罩层
      loading: true,
      // 选中数组
      ids: [],
      // 非单个禁用
      single: true,
      // 非多个禁用
      multiple: true,
      // 显示搜索条件
      showSearch: true,
      // 总条数
      total: 0,
      // 招聘信息表表格数据
      recruitList: [],
      // 表格列信息
      columns: [
        { key: 0, label: '编号', visible: false },
        { key: 1, label: '岗位', visible: true },
        { key: 2, label: '标题链接', visible: true },
        { key: 3, label: '薪资范围', visible: true },
        { key: 4, label: '月薪最小值', visible: false },
        { key: 5, label: '月薪最大值', visible: false },
        { key: 6, label: '月薪平均值', visible: false },
        { key: 7, label: '地点', visible: true },
        { key: 8, label: '经验要求', visible: true },
        { key: 9, label: '学历要求', visible: true },
        { key: 10, label: '技能要求', visible: true },
        { key: 11, label: '企业名称', visible: true },
        { key: 12, label: '上市情况', visible: true },
        { key: 13, label: '企业规模', visible: true },
        { key: 14, label: '主营业务', visible: true },
        { key: 15, label: '标题详情', visible: true },
        { key: 16, label: '薪资范围2', visible: true },
        { key: 17, label: '岗位描述', visible: true },
        { key: 18, label: '工作地点', visible: true }
      ],
      // 弹出层标题
      title: "",
      // 是否显示弹出层
      open: false,
      // 查询参数
      queryParams: {
        pageNum: 1,
        pageSize: 10,
        recruitId: null,
        post: null,
        titleUrl: null,
        location: null,
        experienceRequired: null,
        educationRequired: null,
        skillRequired: null,
        enterpriseName: null,
        listingStatus: null,
        enterpriseSize: null,
        mainBusiness: null,
        titleDetail: null,
      },
      // 表单参数
      form: {},
      // 导入参数
      upload: {
        // 是否显示弹出层（导入）
        open: false,
        // 弹出层标题（导入）
        title: "",
        // 是否禁用上传
        isUploading: false,
        // 是否更新已经存在的招聘信息表数据
        updateSupport: 0,
        // 设置上传的请求头部
        headers: { Authorization: "Bearer " + getToken() },
        // 上传的地址
        url: process.env.VUE_APP_BASE_API + "/recruit/recruit/importData"
      },
      // 表单校验
      rules: {
        recruitId: [
          { required: true, message: "编号不能为空", trigger: "blur" }
        ]
      }
    };
  },
  created() {
    this.getList();
  },
  methods: {
    /** 查询招聘信息表列表 */
    getList() {
      this.loading = true;
      listRecruitInfo(this.queryParams).then(response => {
        this.recruitList = response.rows;
        this.total = response.total;
        this.loading = false;
      });
    },
    // 取消按钮
    cancel() {
      this.open = false;
      this.reset();
    },
    // 表单重置
    reset() {
      this.form = {
        recruitId: null,
        post: null,
        titleUrl: null,
        salaryRange: null,
        salaryMonthMin: null,
        salaryMonthMax: null,
        salaryMonthAvg: null,
        location: null,
        experienceRequired: null,
        educationRequired: null,
        skillRequired: null,
        enterpriseName: null,
        listingStatus: null,
        enterpriseSize: null,
        mainBusiness: null,
        titleDetail: null,
        salaryRange2: null,
        jobDescription: null,
        wordLocation: null
      };
      this.resetForm("form");
    },
    /** 搜索按钮操作 */
    handleQuery() {
      this.queryParams.pageNum = 1;
      this.getList();
    },
    /** 重置按钮操作 */
    resetQuery() {
      this.resetForm("queryForm");
      this.handleQuery();
    },
    // 多选框选中数据
    handleSelectionChange(selection) {
      this.ids = selection.map(item => item.recruitId)
      this.single = selection.length!==1
      this.multiple = !selection.length
    },
    /** 新增按钮操作 */
    handleAdd() {
      this.reset();
      this.open = true;
      this.title = "添加招聘信息表";
    },
    /** 修改按钮操作 */
    handleUpdate(row) {
      this.reset();
      const recruitId = row.recruitId || this.ids
      getRecruitInfo(recruitId).then(response => {
        this.form = response.data;
        this.open = true;
        this.title = "修改招聘信息表";
      });
    },
    /** 提交按钮 */
    submitForm() {
      this.$refs["form"].validate(valid => {
        if (valid) {
          const submitData = this.buildSubmitData();
          if (submitData.recruitId != null) {
            updateRecruitInfo(submitData).then(response => {
              this.$modal.msgSuccess("修改成功");
              this.open = false;
              this.getList();
            });
          } else {
            addRecruitInfo(submitData).then(response => {
              this.$modal.msgSuccess("新增成功");
              this.open = false;
              this.getList();
            });
          }
        }
      });
    },
    /** 删除按钮操作 */
    handleDelete(row) {
      const recruitIds = row.recruitId || this.ids;
      this.$modal.confirm('是否确认删除招聘信息表编号为"' + recruitIds + '"的数据项？').then(function() {
        return delRecruitInfo(recruitIds);
      }).then(() => {
        this.getList();
        this.$modal.msgSuccess("删除成功");
      }).catch(() => {});
    },
    /** 导出按钮操作 */
    handleExport() {
      this.download('recruit/recruit/export', {
        ...this.queryParams
      }, `recruit_${new Date().getTime()}.xlsx`)
    },
    /** 导入按钮操作 */
    handleImport() {
      this.upload.title = "招聘信息表导入";
      this.upload.open = true;
    },
    /** 下载模板操作 */
    importTemplate() {
      this.download(
        "recruit/recruit/importTemplate",
        {},
        "recruit_template_" + new Date().getTime() + ".xlsx"
      );
    },
    // 文件上传中处理
    handleFileUploadProgress(event, file, fileList) {
      this.upload.isUploading = true;
    },
    // 文件上传成功处理
    handleFileSuccess(response, file, fileList) {
      this.upload.open = false;
      this.upload.isUploading = false;
      this.$refs.upload.clearFiles();
      this.$alert("<div style='overflow: auto;overflow-x: hidden;max-height: 70vh;padding: 10px 20px 0;'>" + response.msg + "</div>", "导入结果", { dangerouslyUseHTMLString: true });
      this.getList();
    },
    buildSubmitData() {
      const data = { ...this.form };
      if (data.recruitId !== null && data.recruitId !== undefined && data.recruitId !== "") {
        data.recruitId = parseInt(data.recruitId, 10);
      } else {
        data.recruitId = null;
      }
      if (data.salaryMonthMin !== null && data.salaryMonthMin !== undefined && data.salaryMonthMin !== "") {
        data.salaryMonthMin = parseFloat(data.salaryMonthMin);
      } else {
        data.salaryMonthMin = null;
      }
      if (data.salaryMonthMax !== null && data.salaryMonthMax !== undefined && data.salaryMonthMax !== "") {
        data.salaryMonthMax = parseFloat(data.salaryMonthMax);
      } else {
        data.salaryMonthMax = null;
      }
      if (data.salaryMonthAvg !== null && data.salaryMonthAvg !== undefined && data.salaryMonthAvg !== "") {
        data.salaryMonthAvg = parseFloat(data.salaryMonthAvg);
      } else {
        data.salaryMonthAvg = null;
      }
      return data;
    },
    // 提交上传文件
    submitFileForm() {
      this.$refs.upload.submit();
    }
  }
};
</script>
