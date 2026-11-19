# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 4:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 802 windows, 22076 settled trades, 19 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 410 | 33.7 | 34.9 | $-311.28 | -7.6% | $688.72 | -1.2 | done | can't tell from luck |
| value_ev10 | 1010 | 38.0 | 39.2 | $-634.51 | -6.3% | $365.49 | -1.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 1855 | 50.1 | 49.6 | $-718.05 | -3.9% | $281.95 | -1.7 | done | can't tell from luck |
| trend_filter | 1294 | 50.2 | 50.8 | $-781.84 | -6.0% | $218.16 | -2.2 | done | losing for real |
| reversal_15m_0.10pct | 2258 | 50.9 | 50.6 | $-808.39 | -3.6% | $191.61 | -1.7 | done | can't tell from luck |
| value_ev5 | 1524 | 40.2 | 41.1 | $-860.15 | -5.6% | $139.85 | -1.9 | done | can't tell from luck |
| reversal_60m_0.30pct | 1855 | 49.9 | 51.2 | $-1323.97 | -7.1% | $-323.97 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 3204 | 51.3 | 51.6 | $-1335.06 | -4.2% | $-335.06 | -2.4 | done | losing for real |
| coinflip | 3204 | 50.2 | 50.3 | $-1345.18 | -4.2% | $-345.18 | -2.4 | done | losing for real |
| momentum_15m_0.10pct | 2258 | 49.1 | 50.2 | $-1370.32 | -6.1% | $-370.32 | -2.9 | done | losing for real |
| always_up | 3204 | 47.4 | 49.6 | $-2766.05 | -8.6% | $-1766.05 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5015 | 48.4 | 49.1 | $-2789.69 |
| ETH | 5502 | 48.2 | 48.5 | $-3454.36 |
| SOL | 5749 | 48.3 | 48.6 | $-3158.10 |
| XRP | 5810 | 48.5 | 48.5 | $-2852.67 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
