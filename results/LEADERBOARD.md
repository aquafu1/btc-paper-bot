# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 4:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 371 windows, 10072 settled trades, 44 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 192 | 37.5 | 36.6 | $-14.22 | -0.7% | $985.78 | -0.1 | Sat 9:00 PM | too few trades (192/200) |
| value_ev10 | 490 | 40.6 | 40.5 | $-136.39 | -2.8% | $863.61 | -0.5 | done | can't tell from luck |
| value_ev5 | 722 | 42.0 | 42.1 | $-276.26 | -3.8% | $723.74 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 834 | 49.8 | 49.8 | $-370.55 | -4.4% | $629.45 | -1.3 | done | can't tell from luck |
| trend_filter | 557 | 49.2 | 50.6 | $-387.01 | -6.9% | $612.99 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 1003 | 51.6 | 52.1 | $-485.60 | -4.8% | $514.40 | -1.6 | done | can't tell from luck |
| reversal_60m_0.30pct | 834 | 50.2 | 52.0 | $-609.09 | -7.3% | $390.91 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 1003 | 48.4 | 49.7 | $-625.31 | -6.2% | $374.69 | -2.0 | done | can't tell from luck |
| coinflip | 1479 | 49.8 | 50.8 | $-837.42 | -5.7% | $162.58 | -2.2 | done | losing for real |
| momentum_5m_0.00pct | 1479 | 49.8 | 51.6 | $-1026.70 | -6.9% | $-26.70 | -2.8 | done | losing for real |
| always_up | 1479 | 45.6 | 50.7 | $-2002.52 | -13.5% | $-1002.52 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2269 | 47.3 | 49.4 | $-1808.58 |
| ETH | 2534 | 47.7 | 48.9 | $-1790.52 |
| SOL | 2602 | 48.0 | 49.4 | $-1865.07 |
| XRP | 2667 | 48.8 | 49.1 | $-1306.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
