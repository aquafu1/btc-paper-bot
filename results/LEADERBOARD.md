# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 9:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 775 windows, 21386 settled trades, 43 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 403 | 33.0 | 34.9 | $-381.45 | -9.5% | $618.55 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 2183 | 51.2 | 50.6 | $-645.22 | -3.0% | $354.78 | -1.4 | done | can't tell from luck |
| value_ev10 | 979 | 37.5 | 39.1 | $-744.62 | -7.6% | $255.38 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1807 | 49.8 | 49.6 | $-772.98 | -4.3% | $227.02 | -1.8 | done | can't tell from luck |
| trend_filter | 1257 | 49.9 | 50.8 | $-812.64 | -6.5% | $187.36 | -2.3 | done | losing for real |
| value_ev5 | 1482 | 39.8 | 41.0 | $-975.88 | -6.6% | $24.12 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 1807 | 50.2 | 51.2 | $-1179.11 | -6.5% | $-179.11 | -2.8 | done | losing for real |
| coinflip | 3095 | 50.2 | 50.3 | $-1294.93 | -4.2% | $-294.93 | -2.3 | done | losing for real |
| momentum_15m_0.10pct | 2183 | 48.8 | 50.2 | $-1463.16 | -6.7% | $-463.16 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 3095 | 51.1 | 51.6 | $-1479.38 | -4.8% | $-479.38 | -2.7 | done | losing for real |
| always_up | 3095 | 47.1 | 49.5 | $-2834.72 | -9.2% | $-1834.72 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4851 | 48.2 | 49.1 | $-2950.28 |
| ETH | 5343 | 48.0 | 48.5 | $-3587.35 |
| SOL | 5569 | 48.1 | 48.6 | $-3279.62 |
| XRP | 5623 | 48.5 | 48.5 | $-2766.84 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
