document.addEventListener('DOMContentLoaded', ()=>{
  const circleForm = document.getElementById('circle-form')
  const triangleForm = document.getElementById('triangle-form')
  if(circleForm){
    circleForm.addEventListener('submit', async e=>{
      e.preventDefault()
      const data = new FormData(circleForm)
      const res = await fetch(circleForm.action, {method:'POST', body:data})
      const text = await res.text()
      const el = document.getElementById('circle-result')
      el.classList.toggle('error', !res.ok)
      el.innerText = text
    })
  }
  if(triangleForm){
    triangleForm.addEventListener('submit', async e=>{
      e.preventDefault()
      const data = new FormData(triangleForm)
      const res = await fetch(triangleForm.action, {method:'POST', body:data})
      const text = await res.text()
      const el = document.getElementById('triangle-result')
      el.classList.toggle('error', !res.ok)
      el.innerText = text
    })
  }
})
