# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 4:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 321 windows, 8595 settled trades, 53 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 696 | 53.0 | 51.7 | $-114.25 | -1.6% | $885.75 | -0.5 | done | can't tell from luck |
| value_ev20 | 163 | 33.7 | 36.8 | $-212.09 | -13.0% | $787.91 | -1.3 | Sat 11:15 PM | too few trades (163/200) |
| reversal_15m_0.10pct | 853 | 52.6 | 51.9 | $-247.87 | -2.9% | $752.13 | -0.9 | done | can't tell from luck |
| value_ev10 | 413 | 37.8 | 40.5 | $-449.41 | -10.9% | $550.59 | -1.9 | done | can't tell from luck |
| value_ev5 | 617 | 39.5 | 42.2 | $-649.40 | -10.5% | $350.60 | -2.3 | done | losing for real |
| trend_filter | 476 | 45.0 | 50.4 | $-718.15 | -15.1% | $281.85 | -3.4 | done | losing for real |
| momentum_60m_0.30pct | 696 | 47.0 | 50.0 | $-736.76 | -10.6% | $263.24 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 853 | 47.4 | 49.8 | $-772.10 | -9.1% | $227.90 | -2.7 | done | losing for real |
| coinflip | 1276 | 50.0 | 51.0 | $-783.75 | -6.1% | $216.25 | -2.3 | done | losing for real |
| always_up | 1276 | 47.8 | 50.5 | $-1213.27 | -9.5% | $-213.27 | -3.5 | done | losing for real |
| momentum_5m_0.00pct | 1276 | 48.3 | 51.4 | $-1290.76 | -10.1% | $-290.76 | -3.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1924 | 46.3 | 49.3 | $-2017.62 |
| ETH | 2159 | 46.7 | 48.8 | $-2143.84 |
| SOL | 2238 | 48.1 | 49.4 | $-1754.04 |
| XRP | 2274 | 48.7 | 49.2 | $-1272.31 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
