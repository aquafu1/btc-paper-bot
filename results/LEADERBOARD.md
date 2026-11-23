# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 2:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1178 windows, 32562 settled trades, 47 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 630 | 34.9 | 35.3 | $-352.59 | -5.6% | $647.41 | -1.1 | done | can't tell from luck |
| value_ev10 | 1540 | 38.6 | 39.2 | $-790.38 | -5.1% | $209.62 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3264 | 50.8 | 50.4 | $-1037.79 | -3.2% | $-37.79 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 2745 | 49.6 | 49.4 | $-1210.88 | -4.4% | $-210.88 | -2.3 | done | losing for real |
| value_ev5 | 2333 | 40.2 | 41.1 | $-1279.09 | -5.5% | $-279.09 | -2.2 | done | losing for real |
| trend_filter | 1926 | 48.9 | 50.5 | $-1556.43 | -8.1% | $-556.43 | -3.6 | done | losing for real |
| reversal_60m_0.30pct | 2745 | 50.4 | 51.1 | $-1685.72 | -6.1% | $-685.72 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 3264 | 49.2 | 50.2 | $-1985.04 | -6.1% | $-985.04 | -3.5 | done | losing for real |
| coinflip | 4705 | 50.0 | 50.2 | $-2142.27 | -4.6% | $-1142.27 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 4705 | 50.1 | 51.4 | $-2967.99 | -6.3% | $-1967.99 | -4.5 | done | losing for real |
| always_up | 4705 | 47.8 | 49.3 | $-3479.71 | -7.4% | $-2479.71 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7467 | 48.2 | 49.0 | $-4012.35 |
| ETH | 8083 | 48.1 | 48.4 | $-4826.54 |
| SOL | 8466 | 48.1 | 48.4 | $-4541.22 |
| XRP | 8546 | 48.1 | 48.2 | $-5107.77 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
