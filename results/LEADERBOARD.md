# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 9:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 72 windows, 1789 settled trades, 49 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_5m_0.00pct | 280 | 56.4 | 51.0 | $+199.00 | +7.1% | $1199.00 | +1.2 | done | can't tell from luck |
| reversal_60m_0.30pct | 125 | 60.8 | 52.6 | $+160.78 | +12.9% | $1160.78 | +1.5 | Wed 7:15 PM | too few trades (125/200) |
| reversal_15m_0.10pct | 167 | 56.3 | 51.9 | $+103.07 | +6.2% | $1103.07 | +0.8 | Wed 12:15 PM | too few trades (167/200) |
| value_ev10 | 95 | 43.2 | 39.1 | $+32.23 | +3.4% | $1032.23 | +0.3 | Thu 4:15 AM | too few trades (95/200) |
| value_ev20 | 41 | 34.1 | 35.7 | $-33.85 | -8.3% | $966.15 | -0.4 | Sat 4:45 AM | too few trades (41/200) |
| value_ev5 | 134 | 41.0 | 40.9 | $-65.36 | -4.9% | $934.64 | -0.5 | Wed 5:30 PM | too few trades (134/200) |
| trend_filter | 95 | 45.3 | 48.7 | $-99.47 | -10.5% | $900.53 | -1.0 | Thu 4:15 AM | too few trades (95/200) |
| coinflip | 280 | 50.0 | 51.4 | $-179.25 | -6.4% | $820.75 | -1.1 | done | can't tell from luck |
| momentum_15m_0.10pct | 167 | 43.7 | 49.3 | $-236.99 | -14.2% | $763.01 | -1.8 | Wed 12:15 PM | too few trades (167/200) |
| momentum_60m_0.30pct | 125 | 39.2 | 48.4 | $-267.99 | -21.4% | $732.01 | -2.4 | Wed 7:15 PM | too few trades (125/200) |
| always_up | 280 | 43.6 | 50.4 | $-472.15 | -16.9% | $527.85 | -2.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 372 | 47.3 | 49.8 | $-115.06 |
| ETH | 425 | 46.6 | 48.5 | $-236.37 |
| SOL | 490 | 48.8 | 48.0 | $-289.05 |
| XRP | 502 | 50.2 | 48.2 | $-219.49 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
