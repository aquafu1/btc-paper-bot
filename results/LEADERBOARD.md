# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 7:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 525 windows, 14498 settled trades, 47 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1237 | 51.4 | 49.8 | $-111.76 | -0.9% | $888.24 | -0.3 | done | can't tell from luck |
| value_ev20 | 273 | 35.5 | 35.7 | $-142.64 | -5.2% | $857.36 | -0.7 | done | can't tell from luck |
| value_ev10 | 675 | 38.4 | 39.8 | $-484.70 | -7.2% | $515.30 | -1.5 | done | can't tell from luck |
| trend_filter | 851 | 49.5 | 50.7 | $-551.72 | -6.5% | $448.28 | -1.9 | done | can't tell from luck |
| momentum_15m_0.10pct | 1470 | 49.8 | 49.7 | $-554.06 | -3.8% | $445.94 | -1.4 | done | can't tell from luck |
| value_ev5 | 1006 | 40.4 | 41.5 | $-648.64 | -6.4% | $351.36 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 1470 | 50.2 | 51.5 | $-989.32 | -6.7% | $10.68 | -2.6 | done | losing for real |
| coinflip | 2093 | 50.0 | 50.7 | $-1094.28 | -5.2% | $-94.28 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1237 | 48.6 | 51.4 | $-1188.92 | -9.6% | $-188.92 | -3.5 | done | losing for real |
| momentum_5m_0.00pct | 2093 | 49.3 | 51.6 | $-1691.30 | -8.1% | $-691.30 | -3.8 | done | losing for real |
| always_up | 2093 | 46.3 | 50.1 | $-2429.83 | -11.6% | $-1429.83 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3289 | 47.4 | 49.2 | $-2605.92 |
| ETH | 3614 | 48.0 | 48.7 | $-2354.29 |
| SOL | 3778 | 47.7 | 49.0 | $-2700.79 |
| XRP | 3817 | 48.3 | 48.8 | $-2226.18 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
