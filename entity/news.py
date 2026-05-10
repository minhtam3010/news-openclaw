from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Article:
    article_id: str
    title: str
    link: str
    content: str
    description: Optional[str] = None
    source_id: Optional[str] = None
    source_name: Optional[str] = None
    source_url: Optional[str] = None
    source_icon: Optional[str] = None
    language: Optional[str] = None
    country: Optional[List[str]] = field(default_factory=list)
    category: Optional[List[str]] = field(default_factory=list)
    pubDate: Optional[List[str]] = None
    fetched_at: Optional[List[str]] = None

@dataclass
class NewsResponse:
    status: str
    totalResults: int
    results: List[Article]
    


