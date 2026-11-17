# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 7:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 575 windows, 15914 settled trades, 55 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1354 | 51.3 | 49.7 | $-208.07 | -1.5% | $791.93 | -0.6 | done | can't tell from luck |
| value_ev20 | 309 | 33.3 | 35.2 | $-327.95 | -10.6% | $672.05 | -1.4 | done | can't tell from luck |
| trend_filter | 923 | 50.7 | 51.1 | $-464.64 | -5.0% | $535.36 | -1.6 | done | can't tell from luck |
| value_ev10 | 748 | 37.6 | 39.4 | $-691.32 | -9.2% | $308.68 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 1615 | 51.0 | 51.1 | $-785.29 | -4.9% | $214.71 | -2.0 | done | can't tell from luck |
| value_ev5 | 1120 | 40.0 | 41.3 | $-837.29 | -7.5% | $162.71 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 1615 | 49.0 | 49.8 | $-946.94 | -5.9% | $53.06 | -2.4 | done | losing for real |
| coinflip | 2292 | 49.9 | 50.5 | $-1230.32 | -5.4% | $-230.32 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 1354 | 48.7 | 51.2 | $-1343.84 | -9.9% | $-343.84 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 2292 | 50.3 | 51.9 | $-1553.63 | -6.8% | $-553.63 | -3.4 | done | losing for real |
| always_up | 2292 | 47.1 | 49.9 | $-2286.30 | -10.0% | $-1286.30 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3602 | 47.8 | 49.3 | $-2682.92 |
| ETH | 3971 | 47.9 | 48.6 | $-2712.55 |
| SOL | 4146 | 47.8 | 48.8 | $-3069.59 |
| XRP | 4195 | 48.6 | 48.6 | $-2210.51 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
