// Get manifest URL from query parameter
const urlParams = new URLSearchParams(window.location.search);
const manifestUrl = urlParams.get('manifest');

const assetMapping = {
    hero: 'hero_render',
    cutout: 'product_cutout',
    branded: 'branded_hero',
    billboard: 'billboard',
    video: 'video',
    story: 'story',
    square: 'square',
    banner: 'banner'
};

async function loadManifest() {
    if (!manifestUrl) {
        showError('No manifest URL provided. Add ?manifest=<url> to the URL.');
        return;
    }

    try {
        const response = await fetch(manifestUrl);
        if (!response.ok) throw new Error('Failed to fetch manifest');
        
        const manifest = await response.json();
        displayGallery(manifest);
    } catch (error) {
        console.error('Error loading manifest:', error);
        showError(`Failed to load manifest: ${error.message}`);
    }
}

function displayGallery(manifest) {
    document.getElementById('loading').style.display = 'none';
    document.getElementById('gallery').style.display = 'block';

    // Display job info
    document.getElementById('job-id').textContent = `Job: ${manifest.job_id}`;
    document.getElementById('timestamp').textContent = `Generated: ${new Date(manifest.timestamp).toLocaleString()}`;
    
    // Display brief parameters
    const briefParams = manifest.brief_params;
    document.getElementById('brief-params').innerHTML = `
        <strong>Campaign Brief:</strong><br>
        Mood: ${briefParams.mood || 'N/A'}<br>
        Colors: ${briefParams.colors?.join(', ') || 'N/A'}<br>
        Environment: ${briefParams.environment || 'N/A'}
    `;

    // Load assets
    const assets = manifest.assets;
    
    Object.keys(assetMapping).forEach(key => {
        const assetKey = assetMapping[key];
        const url = assets[assetKey];
        const card = document.getElementById(`card-${key}`);
        
        if (!url) {
            card.style.display = 'none';
            return;
        }

        if (key === 'video') {
            document.getElementById('video-player').src = url;
        } else {
            document.getElementById(`img-${key}`).src = url;
        }

        // Setup download button
        const btn = card.querySelector('.download-btn');
        btn.onclick = () => downloadAsset(url, `${manifest.job_id}_${key}`);
    });
}

function downloadAsset(url, filename) {
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    a.target = '_blank';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
}

function showError(message) {
    document.getElementById('loading').style.display = 'none';
    const errorDiv = document.getElementById('error');
    errorDiv.style.display = 'block';
    errorDiv.querySelector('p').textContent = message;
}

// Load manifest on page load
loadManifest();
