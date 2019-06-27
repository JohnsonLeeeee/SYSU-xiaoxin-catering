const app = getApp()
Page({
  data: {

    items: [{
      id: 4,
      title: '柠檬百香果',
      price: 18,
      active: false,
      num: 1,
      imgUrl: '../menu/image/item4.jpg'
    }]
  },
  onShareAppMessage: function (res) {
    return {
      title: '快来尝尝这道菜吧！',
      path: '/page/user?id=123',
      success: function (res) {
        wx.showModal({
          title: '提示',
          content: '转发成功',
        })
      },
      fail: function (res) {
        wx.showModal({
          title: '提示',
          content: '转发失败',
        })
      }
    }
  }
  
})