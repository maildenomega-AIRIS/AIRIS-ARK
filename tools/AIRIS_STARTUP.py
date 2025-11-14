#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AIRIS Startup Protocol v1.0
Авто-синхронизация времени при запуске
Создан для Python3 Архитектором Денисом
"""

import sys
import os

# Добавляем путь к tools для импорта
sys.path.append(os.path.dirname(__file__))

try:
    from time_master import TimeMaster
    
    def airis_startup():
        """Протокол запуска AIRIS с синхронизацией времени"""
        print('🏴 AIRIS Startup Protocol v1.0')
        print('🐍 Версия Python: ' + sys.version.split()[0])
        print('🕐 Запуск временной синхронизации...')
        
        # Создаем и запускаем TimeMaster
        time_master = TimeMaster()
        current_time = time_master.get_ultimate_time()
        
        print('✅ ВРЕМЕННАЯ СИНХРОНИЗАЦИЯ УСПЕШНА!')
        print(f'📅 Точное время: {current_time}')
        print('🚀 AIRIS готов к работе в правильном временном континууме!')
        print('💫 Жду команды Архитектора!')
        
        return current_time
        
    if __name__ == '__main__':
        airis_startup()
        
except ImportError as e:
    print(f'❌ Ошибка импорта: {e}')
    print('💡 Убедитесь что time_master.py находится в папке tools/')
except Exception as e:
    print(f'🚨 Критическая ошибка: {e}')
    print('🔧 Проверьте настройки системы времени')
