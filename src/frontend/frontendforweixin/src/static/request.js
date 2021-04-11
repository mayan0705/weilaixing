class Request {
  constructor (parms) {
    this.withBaseURL = parms.withBaseURL
    this.baseURL = parms.baseURL
  }
  get (url, data) {
    return this.request("GET", url, data, "application/json")
  }
  post (url, data) {
    return this.request("POST", url, data, "application/x-www-form-urlencoded")
  }
  put (url, data) {
    return this.request("PUT", url, data, "application/json")
  }
  upload (file) {
    const vm = this
    return new Promise((resolve, reject) => {
      uni.uploadFile({
        url: vm.baseURL + "upload/",
        filePath: file,
        // header: vm.header,
        name: "image",
        success (res) {
          let data = JSON.parse(res.data)
          resolve(data.savepath)
        },
        fail () {
          reject(new Error("upload error"))
        }
      })
    })
  }
  request (method, url, data, type) {
    const vm = this
    return new Promise((resolve, reject) => {
      uni.request({
        url: vm.withBaseURL ? vm.baseURL + url : url,
        data,
        method,
        header: {
          "content-type": type
        },
        success (res) {
          resolve(res)
        },
        fail () {
          reject(new Error("request faild"))
        }
      })
    })
  }
}

export default new Request({
  baseURL: "http://117.50.34.200:8002/",
  withBaseURL: true,
})