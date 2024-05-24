const durationFilter = document.getElementById("duration-filter");
const explicitFilter = document.getElementById("explicit-filter");
const searchButton = document.getElementById('search-button');
const searchInput = document.getElementById('search-bar');
const resultsContainer = document.getElementById('results-container');

document.getElementById("reset-filters").addEventListener('click', ()=>{
  durationFilter.value="";
  explicitFilter.checked=false;
});

searchButton.addEventListener('click', () => {

  var searchTerm = searchInput.value;
  var url = `https://itunes.apple.com/search?term=${searchTerm}&entity=song&limit=100`;
  const loadingText = document.getElementById('loading-text');
  loadingText.innerHTML = 'Loading...';
  const noResultsText = document.createElement('p');
  noResultsText.classList.add('no-results-text');
  fetch(url)
    .then(response => response.json())
    .then(data => {
      resultsContainer.innerHTML = '';
      var count=0;
      for (let i = 0; i < data.results.length && i < 200; i++) {
        loadingText.innerHTML = '';
        if(count==10){
          break;
        }
        const result = data.results[i];
        const artistName = result.artistName;
        const trackName = result.trackName;
        const albumName = result.collectionName;
        const artworkUrl = result.artworkUrl100;
        const audioUrl = result.previewUrl;
        const explicit = result.trackExplicitness;
        const duration= result.trackTimeMillis/60000;
        if (explicitFilter.checked && explicit === "explicit") {
          continue; 
        }
        if (durationFilter.value && duration > durationFilter.value ) {
          continue; 
        }

        const card = document.createElement('div');
        card.classList.add('card');
        const content = `
          <img src="${artworkUrl}" alt="${trackName} artwork" class="card-image">
          <div class="card-text"> 
            <h2 class="card-title">${trackName}</h2>
            <p class="card-subtitle">${artistName}</p>
            <p class="card-subtitle">${albumName}</p> 
            <p class="card-subtitle">${explicit}</p>
            <audio controls>
              <source src="${audioUrl}" type="audio/mpeg">
            </audio>
          </div>
        `;
          card.innerHTML = content;
          resultsContainer.appendChild(card);
          count++;
      }
      loadingText.innerHTML = '';
      if (resultsContainer.children.length === 0) {
        noResultsText.textContent = 'No results found for "' + searchTerm + '".';
        resultsContainer.appendChild(noResultsText);
      } else {
        noResultsText.textContent = '';
      }
    })
    .catch(error => console.error(error));
});



