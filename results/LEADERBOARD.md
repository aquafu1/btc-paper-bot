# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 8:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1008 windows, 28057 settled trades, 61 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 518 | 34.2 | 35.0 | $-312.56 | -6.0% | $687.44 | -1.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 2416 | 50.2 | 49.7 | $-894.44 | -3.7% | $105.56 | -1.8 | done | can't tell from luck |
| value_ev10 | 1283 | 37.5 | 39.1 | $-922.99 | -7.2% | $77.01 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 2860 | 50.9 | 50.4 | $-925.32 | -3.2% | $74.68 | -1.7 | done | can't tell from luck |
| trend_filter | 1684 | 49.9 | 50.8 | $-1121.58 | -6.7% | $-121.58 | -2.8 | done | losing for real |
| value_ev5 | 1945 | 39.6 | 41.0 | $-1274.73 | -6.6% | $-274.73 | -2.4 | done | losing for real |
| coinflip | 4025 | 50.5 | 50.4 | $-1644.37 | -4.1% | $-644.37 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 2416 | 49.8 | 51.0 | $-1772.52 | -7.3% | $-772.52 | -3.7 | done | losing for real |
| momentum_15m_0.10pct | 2860 | 49.1 | 50.3 | $-1867.10 | -6.5% | $-867.10 | -3.5 | done | losing for real |
| momentum_5m_0.00pct | 4025 | 50.8 | 51.5 | $-2183.09 | -5.4% | $-1183.09 | -3.6 | done | losing for real |
| always_up | 4025 | 47.3 | 49.5 | $-3629.80 | -9.0% | $-2629.80 | -5.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6403 | 48.3 | 49.0 | $-3510.59 |
| ETH | 6968 | 48.1 | 48.5 | $-4393.04 |
| SOL | 7331 | 48.3 | 48.6 | $-4067.09 |
| XRP | 7355 | 48.1 | 48.4 | $-4577.77 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
