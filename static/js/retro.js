// static/js/retro.js

// 2000年代風のマウスカーソルトレイル効果
document.addEventListener('DOMContentLoaded', function() {
    // ページの読み込み完了メッセージ
    console.log('ページの読み込みが完了しました!');
    
    // 訪問者へのウェルカムアラート (オプション - コメントアウト済)
    // setTimeout(function() {
    //     alert('ようこそ！私の2000年代風ポートフォリオサイトへ！');
    // }, 1000);
    
    // 時計の更新
    updateClock();
    setInterval(updateClock, 60000); // 1分ごとに更新
});

// デジタル時計の更新関数
function updateClock() {
    const clockElements = document.querySelectorAll('.clock');
    const now = new Date();
    const timeString = now.toLocaleString();
    
    clockElements.forEach(function(clock) {
        clock.textContent = timeString;
    });
}

// ページ遷移前の確認 (オプション - コメントアウト済)
// window.onbeforeunload = function() {
//     return 'このページから離れますか？';
// };

// マウスオーバー効果
document.addEventListener('mouseover', function(e) {
    if (e.target.tagName === 'A') {
        e.target.style.cursor = 'pointer';
    }
});