(function () {
  
  [...document.querySelectorAll(".control")].forEach((button) => {
    button.addEventListener("click", function () {
      document.querySelector(".active-btn").classList.remove("active-btn");
      this.classList.add("active-btn");
      // document.querySelector(".active").classList.remove("active");
      console.log(button.dataset.id);
      // document.getElementById(button.dataset.id).focus();
      
    });
  });
  document.querySelector(".theme-btn").addEventListener("click", () => {
    document.body.classList.toggle("light-mode");
  });
  document.querySelector(".theme-btn1").addEventListener("click", () => {
    if(history.back()===undefined){
      window.location.href='/'
    }
    history.back();
  });

})();
const handleTag= (tag) => {
  // window.location.href=`/category/${tag}`
  window.open(`/category/${tag}`, '_blank');
};

const searchCat=()=>{
    let query=document.getElementById('query-category').value;
    let allCategory=document.querySelectorAll('[id^=cat-title-]')
    if(query.trim()=="")
    {
      for(var i=0;i<allCategory.length;i++){
        let id=(allCategory[i].id).substring(10);
          document.getElementById(`category-${id}`).style.display=""
      }
      return
    }
    query=query.split(",")
    for(q in query){
      q=q.trim()
    }
    const lowercaseWords = [];
    query.forEach(word => lowercaseWords.push(word.toLowerCase()));
    console.log(query);
    console.log(allCategory);
    for(var i=0;i<allCategory.length;i++){
      let id=(allCategory[i].id).substring(10);
      console.log(id);
      if(!lowercaseWords.includes(allCategory[i].innerHTML.toLowerCase().trim())){
        document.getElementById(`category-${id}`).style.display="none"
      }else{
        document.getElementById(`category-${id}`).style.display=""
      }
    }
}
const handleBlog=(title)=>{
  console.log(title);
  // window.location.href=`blog/${id}`
  window.open(
    `blog/${title}`,
    '_blank' 
  );
}
const searchTag=()=>{
  let query=document.getElementById('query-category').value;
  let allBlogs=document.querySelectorAll('[id^=blog-]')
  console.log(allBlogs);
  if(query.trim()=="")
  {
    for(var i=0;i<allBlogs.length;i++){
      let id=(allBlogs[i].id).substring(5);
        document.getElementById(`blog-${id}`).style.display=""
    }
    return
  }
  query=query.split(",")
  for(q in query){
    q=q.trim()
  }
  const lowercaseWords = [];
  query.forEach(word => lowercaseWords.push(word.toLowerCase()));
  console.log("que:",query);
  console.log("Lo",lowercaseWords);
  console.log(allBlogs);
  outer:for(var i=0;i<allBlogs.length;i++){
    let id=(allBlogs[i].id).substring(5);
    console.log(id);
    let allCat=document.querySelectorAll(`[id^=tag-${id}-]`)
    console.log("All Cat",allCat);
    for(var j=0;j<allCat.length;j++){
        let name=allCat[j].innerHTML.toLowerCase().trim();
        if(lowercaseWords.includes(name)){
          console.log("Name",name);
          console.log(id);
          document.getElementById(`blog-${id}`).style.display="" 
          continue outer;   
        }
        
    }
    document.getElementById(`blog-${id}`).style.display="none"
    // console.log(id);
    // if(!lowercaseWords.includes(allCategory[i].innerHTML.toLowerCase().trim())){
    //   document.getElementById(`category-${id}`).style.display="none"
    // }else{
    //   document.getElementById(`category-${id}`).style.display=""
    // }
  }
}


