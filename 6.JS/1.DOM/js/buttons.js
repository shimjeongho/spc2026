// 각자의 버튼이 눌릴때마다 위에 div의 값을 가져다가 +1 또는 -1을 한다.
        function increament() {
            console.log('+1 클릭');
            const result = document.getElementById('result');
            // console.log(result);
            let value = parseInt(result.textContent); // 문자를 읽어서 숫자로 바꾼다.
            value = value +1;
            console.log(value);
            result.textContent = value;
        }
        function decreament() {
            console.log('-1 클릭');
            document.getElementById('result').textContent -= 1;
        }

        const button1 = document.getElementById('incButton');
        const button2 = document.getElementById('decButton');

        /* 이벤트 핸들러 */
        button1.addEventListener('click', () => {
           document.getElementById('result').textContent += parseInt(result.textContent) +1;
        });
        button2.addEventListener('click', () => {
           document.getElementById('result').textContent -= 1;
        });