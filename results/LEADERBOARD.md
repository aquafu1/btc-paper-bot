# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 2:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 553 windows, 15339 settled trades, 54 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1307 | 51.3 | 49.7 | $-228.15 | -1.7% | $771.85 | -0.6 | done | can't tell from luck |
| value_ev20 | 302 | 33.4 | 35.2 | $-315.92 | -10.5% | $684.08 | -1.4 | done | can't tell from luck |
| trend_filter | 891 | 50.5 | 51.0 | $-489.63 | -5.5% | $510.37 | -1.7 | done | can't tell from luck |
| value_ev10 | 727 | 37.3 | 39.3 | $-712.65 | -9.8% | $287.35 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 1556 | 49.3 | 49.8 | $-841.16 | -5.4% | $158.84 | -2.1 | done | losing for real |
| value_ev5 | 1081 | 39.7 | 41.2 | $-860.10 | -8.0% | $139.90 | -2.2 | done | losing for real |
| reversal_15m_0.10pct | 1556 | 50.7 | 51.1 | $-880.11 | -5.7% | $119.89 | -2.3 | done | losing for real |
| coinflip | 2204 | 50.0 | 50.5 | $-1228.64 | -5.6% | $-228.64 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 1307 | 48.7 | 51.2 | $-1305.58 | -10.0% | $-305.58 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 2204 | 50.2 | 51.8 | $-1555.61 | -7.1% | $-555.61 | -3.5 | done | losing for real |
| always_up | 2204 | 46.8 | 49.9 | $-2364.81 | -10.7% | $-1364.81 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3468 | 47.5 | 49.2 | $-2801.49 |
| ETH | 3822 | 48.0 | 48.6 | $-2677.55 |
| SOL | 4002 | 47.7 | 48.7 | $-3027.93 |
| XRP | 4047 | 48.5 | 48.6 | $-2275.38 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
