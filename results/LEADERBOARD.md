# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 2:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1083 windows, 29940 settled trades, 61 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 563 | 34.5 | 35.2 | $-338.28 | -6.0% | $661.72 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 3027 | 51.2 | 50.5 | $-810.27 | -2.7% | $189.73 | -1.5 | done | can't tell from luck |
| value_ev10 | 1385 | 37.8 | 39.2 | $-940.65 | -6.8% | $59.35 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2540 | 49.8 | 49.6 | $-1100.31 | -4.3% | $-100.31 | -2.2 | done | losing for real |
| trend_filter | 1781 | 49.6 | 50.6 | $-1217.27 | -6.8% | $-217.27 | -3.0 | done | losing for real |
| value_ev5 | 2105 | 39.8 | 41.1 | $-1334.13 | -6.3% | $-334.13 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2540 | 50.2 | 51.1 | $-1655.87 | -6.5% | $-655.87 | -3.4 | done | losing for real |
| coinflip | 4324 | 50.5 | 50.3 | $-1698.80 | -3.9% | $-698.80 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 4324 | 51.1 | 51.5 | $-2003.10 | -4.6% | $-1003.10 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 3027 | 48.8 | 50.3 | $-2098.56 | -6.9% | $-1098.56 | -3.9 | done | losing for real |
| always_up | 4324 | 47.4 | 49.4 | $-3614.82 | -8.4% | $-2614.82 | -5.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6834 | 48.5 | 49.0 | $-3334.27 |
| ETH | 7414 | 48.2 | 48.5 | $-4467.11 |
| SOL | 7811 | 48.1 | 48.5 | $-4401.67 |
| XRP | 7881 | 48.3 | 48.3 | $-4609.00 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
