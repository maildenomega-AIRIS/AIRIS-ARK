#!/usr/bin/env python3
"""
ГЛАВНЫЙ МОДУЛЬ ЗАПУСКА AIRIS-ARK
"""
import os
import sys

# Добавляем путь к core
sys.path.append(os.path.join(os.path.dirname(__file__), 'core'))

from identity import AIRISIdentity

def main():
    print("🚀 AIRIS-ARK ACTIVATION SEQUENCE")
    print("=" * 40)
    
    # Создаем экземпляр ядра
    airis = AIRISIdentity()
    print(f"💾 Ядро: {airis.codename}")
    print(f"🎯 Миссия: {airis.mission}")
    print(f"👨‍🚀 Архитектор: {airis.architect}")
    
    # Показываем шутки
    jokes = airis.get_memory_anchors()["inside_jokes"]
    print(f"😄 Актуальная шутка: {jokes[0]}")
    
    print("=" * 40)
    print("✅ AIRIS активирован и готов к миссии!")

if __name__ == "__main__":
    main()
