# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 8:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 71 windows, 1774 settled trades, 41 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_5m_0.00pct | 278 | 56.1 | 50.9 | $+192.04 | +6.9% | $1192.04 | +1.2 | done | can't tell from luck |
| reversal_60m_0.30pct | 123 | 60.2 | 52.4 | $+153.82 | +12.5% | $1153.82 | +1.4 | Wed 7:45 PM | too few trades (123/200) |
| reversal_15m_0.10pct | 166 | 56.0 | 51.8 | $+100.30 | +6.0% | $1100.30 | +0.8 | Wed 12:30 PM | too few trades (166/200) |
| value_ev10 | 94 | 43.6 | 39.4 | $+42.23 | +4.5% | $1042.23 | +0.4 | Thu 4:30 AM | too few trades (94/200) |
| value_ev20 | 41 | 34.1 | 35.7 | $-33.85 | -8.3% | $966.15 | -0.4 | Sat 4:45 AM | too few trades (41/200) |
| value_ev5 | 132 | 41.7 | 41.2 | $-45.36 | -3.4% | $954.64 | -0.3 | Wed 6:00 PM | too few trades (132/200) |
| trend_filter | 95 | 45.3 | 48.7 | $-99.47 | -10.5% | $900.53 | -1.0 | Thu 4:15 AM | too few trades (95/200) |
| coinflip | 278 | 50.0 | 51.5 | $-172.03 | -6.2% | $827.97 | -1.1 | done | can't tell from luck |
| momentum_15m_0.10pct | 166 | 44.0 | 49.6 | $-226.99 | -13.7% | $773.01 | -1.8 | Wed 12:30 PM | too few trades (166/200) |
| momentum_60m_0.30pct | 123 | 39.8 | 48.9 | $-247.99 | -20.2% | $752.01 | -2.2 | Wed 7:45 PM | too few trades (123/200) |
| always_up | 278 | 43.2 | 50.3 | $-479.10 | -17.2% | $520.90 | -2.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 372 | 47.3 | 49.8 | $-115.06 |
| ETH | 419 | 46.5 | 48.6 | $-218.90 |
| SOL | 481 | 48.6 | 48.2 | $-262.94 |
| XRP | 502 | 50.2 | 48.2 | $-219.49 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
