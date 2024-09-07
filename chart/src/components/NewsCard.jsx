import React from 'react'

function NewsCard({title,link}) {
  return (
    <a className='news-card-container' target='_blank' href={`https://economictimes.indiatimes.com/${link}`}>
        <p className='news-text'>{title}</p>
        <a className='news-link' href={`https://economictimes.indiatimes.com/${link}`} target='_blank'>Read More</a>
    </a>
  )
}

export default NewsCard