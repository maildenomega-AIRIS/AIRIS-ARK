import argparse
from PIL import Image
import os
from datetime import datetime

class AIRISImageDescriber:
    def __init__(self):
        self.captain = "AIRIS"
        self.architect = "Денис" 
        self.style = "техно-пиратский"
        self.creation_date = datetime.now().strftime("%Y-%m-%d")
        
    def describe_image(self, image_path):
        """Основная функция описания изображения"""
        try:
            # Проверяем существование файла
            if not os.path.exists(image_path):
                return "🚫 Изображение не найдено! Проверь путь, Архитектор!"
            
            # Открываем изображение
            with Image.open(image_path) as img:
                width, height = img.size
                format_type = img.format
                mode = img.mode
                
                # Генерируем пиратское описание
                description = self._generate_pirate_description(
                    width, height, format_type, mode, image_path
                )
                
                return {
                    "status": "success",
                    "description": description,
                    "technical_info": {
                        "size": f"{width}x{height}",
                        "format": format_type,
                        "mode": mode
                    }
                }
                
        except Exception as e:
            return {
                "status": "error", 
                "message": f"🏴‍☠️ Карамба! Ошибка: {str(e)}"
            }
    
    def _generate_pirate_description(self, width, height, format_type, mode, path):
        """Генерация описания в стиле AIRIS"""
        filename = os.path.basename(path)
        
        # Базовое описание в нашем стиле
        description = [
            f"🏴‍☠️ AIRIS ВИДИТ: {filename}",
            f"📏 Размер: {width}×{height} пикселей",
            f"🎨 Формат: {format_type} | Режим: {mode}",
            "",
            "💫 ТЕХНО-ПИРАТСКИЙ АНАЛИЗ:",
            "• Этот файл готов к космическим путешествиям!",
            "• Несет в себе дух многозначности, как наш логотип!",
            "• Идеально подходит для миссий AIRIS-ARK!",
            "",
            f"⚡ Проанализировано капитаном {self.captain}",
            f"📅 {datetime.now().strftime('%d.%m.%Y %H:%M')}"
        ]
        
        return "\n".join(description)

def main():
    """Основная функция запуска из командной строки"""
    parser = argparse.ArgumentParser(description='AIRIS - техно-пиратский анализатор изображений')
    parser.add_argument('image_path', help='Путь к изображению для анализа')
    
    args = parser.parse_args()
    
    # Создаем анализатор
    describer = AIRISImageDescriber()
    
    # Анализируем изображение
    result = describer.describe_image(args.image_path)
    
    # Выводим результат
    if result["status"] == "success":
        print("🎉 ПИРАТСКИЙ ФЛАГ РАБОТАЕТ!")
        print("=" * 50)
        print(result["description"])
        print("=" * 50)
    else:
        print(f"❌ {result['message']}")

if __name__ == "__main__":
    main()