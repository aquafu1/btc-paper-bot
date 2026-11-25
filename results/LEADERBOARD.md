# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 25, 4:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1378 windows, 35782 settled trades, 419 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 716 | 34.2 | 35.3 | $-560.39 | -7.8% | $439.61 | -1.6 | done | can't tell from luck |
| value_ev10 | 1736 | 38.7 | 39.1 | $-819.44 | -4.7% | $180.56 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3576 | 50.8 | 50.1 | $-1050.52 | -2.9% | $-50.52 | -1.8 | done | can't tell from luck |
| value_ev5 | 2614 | 40.4 | 41.1 | $-1331.53 | -5.1% | $-331.53 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 3000 | 50.8 | 50.9 | $-1508.09 | -5.0% | $-508.09 | -2.8 | done | losing for real |
| momentum_60m_0.30pct | 3000 | 49.2 | 49.3 | $-1516.17 | -5.1% | $-516.17 | -2.8 | done | losing for real |
| trend_filter | 2126 | 48.4 | 50.4 | $-1907.96 | -9.0% | $-907.96 | -4.2 | done | losing for real |
| momentum_15m_0.10pct | 3576 | 49.2 | 50.2 | $-2187.59 | -6.1% | $-1187.59 | -3.7 | done | losing for real |
| coinflip | 5146 | 50.0 | 50.0 | $-2232.06 | -4.3% | $-1232.06 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 5146 | 50.1 | 51.3 | $-3226.89 | -6.3% | $-2226.89 | -4.6 | done | losing for real |
| always_up | 5146 | 47.9 | 49.3 | $-3698.93 | -7.2% | $-2698.93 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8892 | 47.9 | 48.8 | $-5151.81 |
| ETH | 9580 | 48.0 | 48.1 | $-5303.53 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
