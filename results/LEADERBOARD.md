# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 24, 3:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1277 windows, 34305 settled trades, 388 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 671 | 34.1 | 35.3 | $-520.36 | -7.8% | $479.64 | -1.5 | done | can't tell from luck |
| value_ev10 | 1645 | 38.6 | 39.2 | $-833.77 | -5.1% | $166.23 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3440 | 50.6 | 50.2 | $-1203.73 | -3.5% | $-203.73 | -2.1 | done | losing for real |
| value_ev5 | 2488 | 40.4 | 41.1 | $-1285.12 | -5.2% | $-285.12 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2875 | 49.5 | 49.4 | $-1323.43 | -4.6% | $-323.43 | -2.5 | done | losing for real |
| trend_filter | 2033 | 49.0 | 50.5 | $-1623.73 | -8.0% | $-623.73 | -3.7 | done | losing for real |
| reversal_60m_0.30pct | 2875 | 50.5 | 51.0 | $-1672.79 | -5.8% | $-672.79 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 3440 | 49.4 | 50.2 | $-2038.17 | -5.9% | $-1038.17 | -3.5 | done | losing for real |
| coinflip | 4946 | 49.9 | 50.1 | $-2297.00 | -4.6% | $-1297.00 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 4946 | 50.5 | 51.4 | $-2800.43 | -5.7% | $-1800.43 | -4.1 | done | losing for real |
| always_up | 4946 | 47.8 | 49.3 | $-3674.84 | -7.4% | $-2674.84 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8172 | 48.0 | 48.9 | $-4876.34 |
| ETH | 8823 | 48.2 | 48.3 | $-4812.80 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
