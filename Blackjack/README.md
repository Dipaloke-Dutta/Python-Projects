_**RULES**_

_**Basic Blackjack Game Rules in Python**_
1. The game uses a deck represented by the list:
   [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10,[10][10], where 11 is an Ace, and tens plus face cards (Jack, Queen, King) count as 10.
2. Both the player ("user") and dealer ("comp") are dealt two cards at the start.
3. Aces (11) can be counted as 1 if the player's total would otherwise bust (go over 21).
4. Player can "hit" (draw another card) or "stand" (hold their hand and let the dealer play).
5. The dealer must hit until their hand's value is at least 17.
6. A "blackjack" is a two-card hand totaling 21 (Ace + 10-value card)—instant win for the player unless the dealer also has blackjack.
7. If the player's hand exceeds 21, it's a "bust" and the player loses the round.
8. After the player stands, the dealer plays their hand:
9. If the dealer busts (over 21), the player wins.
10. If dealer and player have equal totals, it's a draw.
11. ighest total (not over 21) wins.

_**Player Choices**_
->Hit: Add a card to your hand. If total goes over 21, you bust and lose the round.
->Stand: Play passes to the dealer, who follows fixed rules described above.

_**Special Rules**_
i. If either player's initial hand totals 21, it's an automatic win ("Blackjack!").
ii. Multiple aces are correctly converted as needed to prevent busting.
iii. Dealer's hand initially shows only one card until the round is finished.

_**Game Flow**_
The game displays a logo and asks whether you want to play.
Cards are dealt; scores are shown; partial dealer's hand is revealed.
You can hit or stand until you bust, reach 21, or choose to stand.
After the player's turn, the dealer completes their hand according to the rules.
Round ends with win, lose, or draw announcement, then can repeat.
