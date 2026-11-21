# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 7:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1006 windows, 27992 settled trades, 58 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 518 | 34.2 | 35.0 | $-312.56 | -6.0% | $687.44 | -1.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 2852 | 51.1 | 50.4 | $-845.32 | -3.0% | $154.68 | -1.6 | done | can't tell from luck |
| value_ev10 | 1282 | 37.4 | 39.1 | $-934.13 | -7.3% | $65.87 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2408 | 50.0 | 49.7 | $-979.66 | -4.1% | $20.34 | -2.0 | done | can't tell from luck |
| trend_filter | 1677 | 49.7 | 50.8 | $-1196.09 | -7.1% | $-196.09 | -3.0 | done | losing for real |
| value_ev5 | 1944 | 39.6 | 41.0 | $-1285.86 | -6.6% | $-285.86 | -2.5 | done | losing for real |
| coinflip | 4017 | 50.5 | 50.3 | $-1664.38 | -4.1% | $-664.38 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2408 | 50.0 | 51.0 | $-1692.52 | -7.0% | $-692.52 | -3.5 | done | losing for real |
| momentum_15m_0.10pct | 2852 | 48.9 | 50.3 | $-1952.32 | -6.8% | $-952.32 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 4017 | 50.7 | 51.5 | $-2247.60 | -5.6% | $-1247.60 | -3.7 | done | losing for real |
| always_up | 4017 | 47.1 | 49.5 | $-3715.02 | -9.2% | $-2715.02 | -5.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6388 | 48.2 | 49.0 | $-3562.77 |
| ETH | 6950 | 48.0 | 48.5 | $-4472.60 |
| SOL | 7315 | 48.2 | 48.6 | $-4125.28 |
| XRP | 7339 | 48.1 | 48.4 | $-4664.82 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
