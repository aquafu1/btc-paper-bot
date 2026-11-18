# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 2:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 697 windows, 19261 settled trades, 70 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 369 | 34.1 | 34.9 | $-239.86 | -6.5% | $760.14 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1621 | 50.4 | 49.5 | $-433.32 | -2.7% | $566.68 | -1.1 | done | can't tell from luck |
| value_ev10 | 891 | 38.4 | 39.1 | $-504.89 | -5.7% | $495.11 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 1978 | 51.5 | 50.8 | $-567.57 | -2.9% | $432.43 | -1.3 | done | can't tell from luck |
| value_ev5 | 1340 | 40.9 | 41.1 | $-580.11 | -4.3% | $419.89 | -1.3 | done | can't tell from luck |
| trend_filter | 1123 | 50.4 | 50.9 | $-596.36 | -5.3% | $403.64 | -1.8 | done | can't tell from luck |
| coinflip | 2780 | 50.1 | 50.3 | $-1209.36 | -4.4% | $-209.36 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1621 | 49.6 | 51.3 | $-1272.98 | -7.9% | $-272.98 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 1978 | 48.5 | 50.0 | $-1340.36 | -6.8% | $-340.36 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 2780 | 50.9 | 51.8 | $-1454.97 | -5.2% | $-454.97 | -2.9 | done | losing for real |
| always_up | 2780 | 47.4 | 49.5 | $-2334.58 | -8.4% | $-1334.58 | -4.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4365 | 48.3 | 49.1 | $-2503.23 |
| ETH | 4797 | 48.3 | 48.5 | $-2710.35 |
| SOL | 5024 | 48.2 | 48.6 | $-2897.51 |
| XRP | 5075 | 48.6 | 48.4 | $-2423.27 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
