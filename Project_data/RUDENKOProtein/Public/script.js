document.addEventListener("DOMContentLoaded", () => {
    console.log("Script running...");

    const form = document.getElementById('order-form');
    if (!form) {
        console.error('No form element found!');
        return;
    }

    // Карусель
    let currentIndex = 0;
    const images = document.querySelectorAll('.carousel img');
    const totalImages = images.length;

    console.log(`Total Images: ${totalImages}`);
    if (totalImages > 0) {
        setInterval(() => {
            console.log(`Switching from image ${currentIndex}`);
            images[currentIndex].classList.remove('active');
            currentIndex = (currentIndex + 1) % totalImages;
            images[currentIndex].classList.add('active');
            console.log(`Switched to image ${currentIndex}`);
        }, 3000);
    }

    // Обработка формы при отправке
    form.addEventListener('submit', (event) => {
        event.preventDefault();  // предотвратить перезагрузку страницы

        const formData = {
            name: document.getElementById('name').value,
            phone: document.getElementById('phone').value
        };

        console.log('Form Data being sent:', formData);

        // Отправка данных через AJAX
        $.ajax({
            url: '/api/data',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(formData),
            success: (response) => {
                console.log('Response from server:', response);
            },
            error: (jqXHR, textStatus, errorThrown) => {
                console.error('AJAX Error:', textStatus, errorThrown);
            }
        });
    });

    // Кнопка "вверх"
    const scrollButton = document.getElementById('btntotop');
    if (scrollButton) {
        window.onscroll = function () {
            if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
                scrollButton.style.display = 'block';
            } else {
                scrollButton.style.display = 'none';
            }
        };

        scrollButton.onclick = function () {
            document.body.scrollTop = 0;
            document.documentElement.scrollTop = 0;
        };
    }
});
