# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 10:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 538 windows, 14890 settled trades, 57 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1274 | 51.6 | 49.8 | $-132.53 | -1.0% | $867.47 | -0.4 | done | can't tell from luck |
| value_ev20 | 284 | 34.2 | 35.5 | $-252.64 | -8.9% | $747.36 | -1.2 | done | can't tell from luck |
| trend_filter | 871 | 50.6 | 50.9 | $-426.33 | -4.9% | $573.67 | -1.5 | done | can't tell from luck |
| momentum_15m_0.10pct | 1508 | 50.1 | 49.8 | $-550.49 | -3.7% | $449.51 | -1.4 | done | can't tell from luck |
| value_ev10 | 698 | 37.5 | 39.7 | $-660.63 | -9.5% | $339.37 | -2.1 | done | losing for real |
| value_ev5 | 1041 | 39.7 | 41.4 | $-866.07 | -8.3% | $133.93 | -2.3 | done | losing for real |
| reversal_15m_0.10pct | 1508 | 49.9 | 51.3 | $-1135.63 | -7.5% | $-135.63 | -3.0 | done | losing for real |
| coinflip | 2144 | 49.8 | 50.6 | $-1248.19 | -5.8% | $-248.19 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 1274 | 48.4 | 51.3 | $-1311.97 | -10.3% | $-311.97 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 2144 | 50.1 | 51.7 | $-1505.47 | -7.0% | $-505.47 | -3.4 | done | losing for real |
| always_up | 2144 | 46.6 | 50.1 | $-2439.09 | -11.4% | $-1439.09 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3374 | 47.5 | 49.3 | $-2729.41 |
| ETH | 3713 | 48.1 | 48.7 | $-2487.99 |
| SOL | 3883 | 47.7 | 48.9 | $-2962.19 |
| XRP | 3920 | 48.4 | 48.8 | $-2349.45 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
