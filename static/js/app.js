var tips = function ($msg, $type, $icon, $from, $align) {
	$type  = $type || 'info';
	$from  = $from || 'top';
	$align = $align || 'center';
	$enter = $type == 'success' ? 'animated fadeInUp' : 'animated shake';

	jQuery.notify({
		icon: $icon,
		message: $msg
	},
	{
		element: 'body',
		type: $type,
		allow_dismiss: true,
		newest_on_top: true,
		showProgressbar: false,
		placement: {
			from: $from,
			align: $align
		},
		offset: 20,
		spacing: 10,
		z_index: 10800,
		delay: 3000,
		timer: 1000,
		animate: {
			enter: $enter,
			exit: 'animated fadeOutDown'
		}
	});
};

/**
 * 页面加载等待
 * @param $mode 'show', 'hide'
 * @author yinq
 */
var pageLoader = function ($mode) {
	var $loadingEl = jQuery('#loader-wrapper');
	$mode          = $mode || 'show';

	if ($mode === 'show') {
		if ($loadingEl.length) {
			$loadingEl.fadeIn(250);
		} else {
			jQuery('body').prepend('<div id="loader-wrapper"><div id="loader"></div></div>');
		}
	} else if ($mode === 'hide') {
		if ($loadingEl.length) {
			$loadingEl.fadeOut(250);
		}
	}

	return false;
};

// 下单
$('#orders-modal').on('show.bs.modal', function (event) {
	var button = $(event.relatedTarget);
	var title = button.data('title');
	var sid = button.data('sid');
	var modal = $(this);
	var submitSignInBtn = modal.find('.modal-body button');

	modal.find('.modal-title').text(title);
	submitSignInBtn.data('sid', sid);
});

$('button.orders').click(function () {

	var name = $.trim($('input#name').val());
	var contact_info = $.trim($('input#contact-info').val());

	if (name === '' || contact_info === ''){
		tips('姓名、联系信息都不能为空', 'danger');
		return false;
	}


	var contact_way = $('select#contact-way').val();
	var sid = $(this).data('sid');
	console.log(contact_info);
	$.ajax({
		cache: false,
		type: 'POST',
		url: '/service/list/',
		data: {'sid':sid, 'name': name, 'way': contact_way, 'info': contact_info},
		async: true,
		success: function (data) {
			if(data['msg'] === 'ok'){
				tips('下单成功, 页面即将刷新~', 'success');
				setTimeout(function () {
					location.reload();
				}, 1500);
			} else {
				tips('订阅失败, 请稍后重试', 'danger');
				setTimeout(function () {
					location.reload();
				}, 1500);
			}
		}
	});
});

function uploadImageToQiNiu(file, username, token, sort, postUrl, data) {
	var key = sort + '/' + username + '/' + hex_md5(new Date().getTime() + file.name) + '.' + file.name.split('.')[1];
	console.log(postUrl);

	var putExtra = {
		fname: "",
		params: {},
		mimeType: null
	};
	var config = {
	  useCdnDomain: true,
	  retryCount: 6
	};
	var next = function () {
		// 暂无相关操作, 原本是用来显示加载圈圈的
	};
	var error = function () {
		pageLoader('hide');
		subscription.unsubscribe();
		tips('上传失败~', 'danger');
		setTimeout(function () {
			location.reload();
		}, 1500);
	};
	var complete = function (res) {
		data['srcUrl'] = res.key;
		uploadInfo(postUrl, data);
	};
	var observer = {
		next: next,
		error: error,
		complete: complete
	};

	var observable = qiniu.upload(file, key, token, putExtra, config);
	// 开始上传
	var subscription = observable.subscribe(observer);
}

function uploadInfo(postUrl, data) {
	$.ajax({
		cache: false,
		type: 'POST',
		url: postUrl,
		data: data,
		success: function (response) {
			response.msg === 'ok' ? tips('添加成功~', 'success') : tips('添加失败~', 'danger');
		},
		complete: function () {
			setTimeout(function () {
				location.reload();
			}, 1500);
		}
	});
}