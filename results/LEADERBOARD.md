# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 5:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1236 windows, 33698 settled trades, 439 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 660 | 34.4 | 35.3 | $-474.16 | -7.2% | $525.84 | -1.4 | done | can't tell from luck |
| value_ev10 | 1612 | 38.7 | 39.2 | $-780.67 | -4.8% | $219.33 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3379 | 50.8 | 50.2 | $-1069.63 | -3.2% | $-69.63 | -1.8 | done | can't tell from luck |
| value_ev5 | 2437 | 40.4 | 41.1 | $-1247.46 | -5.1% | $-247.46 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2826 | 49.5 | 49.4 | $-1269.75 | -4.5% | $-269.75 | -2.4 | done | losing for real |
| trend_filter | 1993 | 48.8 | 50.4 | $-1670.11 | -8.4% | $-670.11 | -3.8 | done | losing for real |
| reversal_60m_0.30pct | 2826 | 50.5 | 51.1 | $-1681.52 | -6.0% | $-681.52 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 3379 | 49.2 | 50.2 | $-2094.62 | -6.2% | $-1094.62 | -3.6 | done | losing for real |
| coinflip | 4862 | 50.0 | 50.1 | $-2206.53 | -4.5% | $-1206.53 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 4862 | 50.2 | 51.4 | $-2961.28 | -6.1% | $-1961.28 | -4.4 | done | losing for real |
| always_up | 4862 | 47.8 | 49.3 | $-3595.83 | -7.4% | $-2595.83 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7878 | 48.0 | 48.9 | $-4528.97 |
| ETH | 8510 | 48.1 | 48.3 | $-4938.37 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
