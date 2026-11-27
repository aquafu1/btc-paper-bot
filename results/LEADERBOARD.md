# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 27, 6:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1576 windows, 38416 settled trades, 401 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 804 | 34.5 | 35.2 | $-571.63 | -7.1% | $428.37 | -1.5 | done | can't tell from luck |
| value_ev10 | 1904 | 38.6 | 39.1 | $-950.92 | -5.0% | $49.08 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3798 | 50.9 | 50.0 | $-951.13 | -2.5% | $48.87 | -1.5 | done | can't tell from luck |
| value_ev5 | 2858 | 40.5 | 41.0 | $-1400.29 | -4.9% | $-400.29 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 3183 | 51.0 | 50.9 | $-1493.91 | -4.7% | $-493.91 | -2.7 | done | losing for real |
| momentum_60m_0.30pct | 3183 | 49.0 | 49.2 | $-1687.95 | -5.3% | $-687.95 | -3.0 | done | losing for real |
| trend_filter | 2262 | 48.5 | 50.3 | $-1981.52 | -8.8% | $-981.52 | -4.3 | done | losing for real |
| coinflip | 5542 | 50.0 | 49.9 | $-2365.62 | -4.3% | $-1365.62 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 3798 | 49.1 | 50.2 | $-2379.09 | -6.3% | $-1379.09 | -3.9 | done | losing for real |
| momentum_5m_0.00pct | 5542 | 50.1 | 51.3 | $-3480.13 | -6.3% | $-2480.13 | -4.8 | done | losing for real |
| always_up | 5542 | 48.2 | 49.2 | $-3513.28 | -6.3% | $-2513.28 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10151 | 48.0 | 48.6 | $-5660.99 |
| ETH | 10955 | 48.0 | 47.7 | $-5530.25 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
