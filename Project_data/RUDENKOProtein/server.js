const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');

const app = express();
const PORT = process.env.PORT || 3000;

// Парсер для JSON данных
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Используем express для статики (отправка файлов из папки public)
app.use(express.static(path.join(__dirname, 'public')));

// Путь для получение данных формы по POST запросу
app.post('/api/data', (req, res) => {
    const { name, phone } = req.body; // обрабатываем нужные поля

    // Валидация обязательных полей
    if (!name || !phone) {
        return res.status(400).json({ message: 'Пожалуйста, заполните все обязательные поля.' });
    }

    console.log('Received form data:', { name, phone });

    res.json({ message: 'Form data received successfully' });
});

// Обслуживание остальных GET запросов для просмотра index.html
app.get('*', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Запуск сервера
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
