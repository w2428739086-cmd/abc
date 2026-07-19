import random
import time

# 单词库（英文 -> 中文）
word_bank = {
 "apple": "苹果",
 "book": "书本",
 "cat": "猫",
 "dog": "狗",
 "elephant": "大象",
 "flower": "花朵",
 "garden": "花园",
 "happy": "快乐的",
 "ice": "冰",
 "jungle": "丛林",
 "knowledge": "知识",
 "love": "爱",
 "moon": "月亮",
 "night": "夜晚",
 "ocean": "海洋",
 "pencil": "铅笔",
 "quiet": "安静的",
 "rainbow": "彩虹",
 "sun": "太阳",
 "tree": "树"
}

def word_game():
 """单词记忆小游戏"""
 print("=" * 40)
 print("🎯 欢迎来到单词记忆小游戏！")
 print("=" * 40)
 print("我会显示一个英文单词，请说出它的中文意思")
 print("输入 'quit' 可以退出游戏\n")

 score = 0
 total = 0
 words_list = list(word_bank.items())

 while True:
 # 随机选择一个单词
 english, chinese = random.choice(words_list)

 # 显示英文单词
 print(f"📝 英文单词：{english}")
 user_answer = input("👉 请输入中文意思：").strip()

 # 退出检查
 if user_answer.lower() == 'quit':
 print(f"\n👋 游戏结束！你答对了 {score}/{total} 题")
 if total > 0:
 accuracy = (score / total) * 100
 print(f"正确率：{accuracy:.1f}%")

 # 根据正确率给出评价
 if accuracy >= 80:
 print("🌟 太棒了！你是单词大师！")
 elif accuracy >= 60:
 print("👍 不错哦！继续加油！")
 else:
 print("💪 多多练习，你会越来越好的！")
 break

 total += 1

 # 判断答案是否正确（忽略大小写和前后空格）
 if user_answer == chinese:
 print("✅ 正确！太棒了！\n")
 score += 1
 else:
 print(f"❌ 哎呀，正确答案是：{chinese}\n")

 # 短暂停顿，让玩家看清结果
 time.sleep(0.5)

# 运行游戏
if __name__ == "__main__":
 word_game()
