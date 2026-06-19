import json
from datetime import datetime
from typing import Dict, List, Optional

# 站点资料条目结构
SITE_ENTRIES: List[Dict[str, object]] = [
    {
        "site_id": "site_001",
        "title": "乐鱼体育官方入口",
        "url": "https://homeportal-leyu.com.cn",
        "tags": ["体育", "娱乐", "赛事直播"],
        "brief": "乐鱼体育官方入口平台，提供最新体育赛事直播、比分预测及互动娱乐服务。",
        "keywords": ["乐鱼体育", "体育直播", "赛事竞猜"]
    },
    {
        "site_id": "site_002",
        "title": "乐鱼体育资讯中心",
        "url": "https://homeportal-leyu.com.cn/news",
        "tags": ["资讯", "体育新闻", "赛事分析"],
        "brief": "汇集全球体育新闻、深度赛事分析与独家专家观点。",
        "keywords": ["乐鱼体育", "体育资讯", "赛事解读"]
    },
    {
        "site_id": "site_003",
        "title": "乐鱼体育社区",
        "url": "https://homeportal-leyu.com.cn/community",
        "tags": ["社区", "互动", "用户生成内容"],
        "brief": "体育爱好者的互动社区，讨论比赛、分享心得、组建战队。",
        "keywords": ["乐鱼体育", "体育社区", "球迷互动"]
    }
]

def format_tag_block(tags: List[str]) -> str:
    """将标签列表格式化为带标记的字符串块"""
    cleaned = [t.strip() for t in tags if t.strip()]
    if not cleaned:
        return "[未标注]"
    return " | ".join(cleaned)

def format_keywords_block(keywords: List[str]) -> str:
    """将关键词列表格式化为逗号分隔的字符串"""
    if not keywords:
        return "（无关键词）"
    return "、".join(keywords)

def build_site_summary(entry: Dict) -> str:
    """根据单条站点资料生成结构化摘要"""
    lines = []
    lines.append(f"站点名称：{entry.get('title', '未命名')}")
    lines.append(f"访问地址：{entry.get('url', '未提供')}")
    lines.append(f"内容标签：{format_tag_block(entry.get('tags', []))}")
    lines.append(f"核心关键词：{format_keywords_block(entry.get('keywords', []))}")
    lines.append(f"简要说明：{entry.get('brief', '暂无说明')}")
    return "\n".join(lines)

def generate_full_report(entries: List[Dict], generate_time: Optional[str] = None) -> str:
    """生成所有站点资料的结构化摘要报告"""
    if generate_time is None:
        generate_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    header = f"【站点资料结构化摘要报告】\n生成时间：{generate_time}\n总条目数：{len(entries)}\n"
    separator = "=" * 48
    parts = [header, separator]

    for idx, entry in enumerate(entries, start=1):
        summary = build_site_summary(entry)
        block = f"项 {idx:02d}\n{summary}\n{separator}"
        parts.append(block)

    return "\n".join(parts)

def export_report_to_file(content: str, filename: str = "site_summary_output.txt") -> None:
    """将生成的报告写入文本文件"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[OK] 报告已写入文件：{filename}")

def run_summary_pipeline() -> None:
    """主流程：读取配置数据、生成摘要、输出到控制台和文件"""
    report_content = generate_full_report(SITE_ENTRIES)

    print("\n" + "=" * 56)
    print("开始输出站点资料摘要")
    print("=" * 56)
    print(report_content)
    print("=" * 56)

    export_report_to_file(report_content)

if __name__ == "__main__":
    run_summary_pipeline()