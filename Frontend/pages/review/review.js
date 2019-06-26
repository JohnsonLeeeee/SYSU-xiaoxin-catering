// pages/review/review.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    reviews: [{
      uname: 'USER1',
      flag: 4,
      image: 'image/item-m.jpg',
      comment: 'A nice canteen!'
    }, {
      uname: 'USER2',
      flag:3,
      image: 'image/item-m.jpg',
      comment: 'It\'s quite far from home...yet I appreciate the cook here!'
    }, {
      uname: 'USER3',
      flag:5,
      image: 'image/item-m.jpg',
      comment: 'I like this one'
    }],
    tempcomment: ''
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {
    //getcomments();
  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  },
  submit: function (event) {
    str = event.target.dataset.text;
    this.setdata({
      tempcomment: str
    });
    //sendcomments(str);
  },
  getcomments: function () {
    wx.request({
      url: '/v1/comment/<:rid>',
      method: 'GET',
      success(res) {
        console.log(res.data);
        this.setdata({
          reviews: res
        });
      }
    })
  },
  sendcomments: function (str) {
    wx.request({
      url: '/v1/comment/<:rid>',
      method: 'POST',
      header: {
        uid: 1,
        content: str
      },
      success(res) {
        console.log(res.data);
      }
    })
  },
  gotowrite: function () {
    wx.redirectTo({
      url: 'write/writecomment',
    })
  }
})