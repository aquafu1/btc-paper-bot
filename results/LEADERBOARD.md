# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 9:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 74 windows, 1845 settled trades, 42 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_5m_0.00pct | 289 | 56.4 | 51.0 | $+209.48 | +7.2% | $1209.48 | +1.3 | done | can't tell from luck |
| reversal_60m_0.30pct | 128 | 61.7 | 52.5 | $+194.98 | +15.2% | $1194.98 | +1.8 | Wed 8:00 PM | too few trades (128/200) |
| reversal_15m_0.10pct | 174 | 56.9 | 51.9 | $+129.62 | +7.4% | $1129.62 | +1.0 | Wed 12:15 PM | too few trades (174/200) |
| value_ev10 | 99 | 43.4 | 39.5 | $+29.52 | +3.0% | $1029.52 | +0.2 | Thu 4:15 AM | too few trades (99/200) |
| value_ev20 | 41 | 34.1 | 35.7 | $-33.85 | -8.3% | $966.15 | -0.4 | Sat 8:30 AM | too few trades (41/200) |
| value_ev5 | 138 | 41.3 | 41.1 | $-68.07 | -4.9% | $931.93 | -0.5 | Wed 5:45 PM | too few trades (138/200) |
| trend_filter | 96 | 44.8 | 48.7 | $-109.47 | -11.4% | $890.53 | -1.1 | Thu 5:30 AM | too few trades (96/200) |
| coinflip | 289 | 49.8 | 51.4 | $-188.45 | -6.5% | $811.55 | -1.1 | done | can't tell from luck |
| momentum_15m_0.10pct | 174 | 43.1 | 49.4 | $-267.58 | -15.4% | $732.42 | -2.0 | Wed 12:15 PM | too few trades (174/200) |
| momentum_60m_0.30pct | 128 | 38.3 | 48.6 | $-297.99 | -23.3% | $702.01 | -2.6 | Wed 8:00 PM | too few trades (128/200) |
| always_up | 289 | 44.3 | 50.3 | $-437.22 | -15.1% | $562.78 | -2.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 394 | 47.0 | 49.7 | $-164.56 |
| ETH | 435 | 46.7 | 48.6 | $-234.87 |
| SOL | 504 | 49.2 | 48.1 | $-242.98 |
| XRP | 512 | 50.4 | 48.3 | $-196.60 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
