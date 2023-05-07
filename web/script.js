const letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];

const letterElement = document.getElementById('letter');
const startBtn = document.getElementById('startBtn');
const timerBar = document.getElementById('timer-bar');

let usedLetters = new Set();
let timerInterval;

function getUnusedLetter() {
  let unusedLetters = letters.filter(letter => !usedLetters.has(letter));
  if (unusedLetters.length === 0) {
    usedLetters.clear();
    unusedLetters = letters;
  }
  const letter = unusedLetters[Math.floor(Math.random() * unusedLetters.length)];
  usedLetters.add(letter);
  return letter;
}

function startGame() {
  const letter = getUnusedLetter();
  letterElement.textContent = letter;
  timerBar.style.width = '100%';
  clearInterval(timerInterval);
  let timeLeft = 5;
  timerInterval = setInterval(() => {
    timeLeft--;
    const width = (timeLeft / 5) * 100;
    timerBar.style.width = `${width}%`;
    if (timeLeft === 0) {
      clearInterval(timerInterval);
      letterElement.textContent = '';
      timerBar.style.width = '0%';
      alert('You LOSE!');
    }
  }, 1000);
}

startBtn.addEventListener('click', startGame);

