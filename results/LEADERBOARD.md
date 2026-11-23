# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 12:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1218 windows, 33442 settled trades, 358 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 652 | 34.5 | 35.3 | $-443.45 | -6.8% | $556.55 | -1.3 | done | can't tell from luck |
| value_ev10 | 1598 | 38.7 | 39.2 | $-776.01 | -4.9% | $223.99 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3352 | 50.8 | 50.3 | $-1089.37 | -3.2% | $-89.37 | -1.9 | done | can't tell from luck |
| value_ev5 | 2416 | 40.5 | 41.1 | $-1191.23 | -4.9% | $-191.23 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2806 | 49.5 | 49.4 | $-1271.91 | -4.5% | $-271.91 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 2806 | 50.5 | 51.1 | $-1674.93 | -6.0% | $-674.93 | -3.2 | done | losing for real |
| trend_filter | 1979 | 48.7 | 50.4 | $-1682.12 | -8.5% | $-682.12 | -3.9 | done | losing for real |
| momentum_15m_0.10pct | 3352 | 49.2 | 50.2 | $-2060.63 | -6.1% | $-1060.63 | -3.6 | done | losing for real |
| coinflip | 4827 | 50.0 | 50.1 | $-2205.40 | -4.6% | $-1205.40 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 4827 | 50.2 | 51.4 | $-2955.48 | -6.1% | $-1955.48 | -4.4 | done | losing for real |
| always_up | 4827 | 47.8 | 49.3 | $-3544.44 | -7.3% | $-2544.44 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7761 | 48.1 | 48.9 | $-4342.06 |
| ETH | 8371 | 48.0 | 48.3 | $-4968.67 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
