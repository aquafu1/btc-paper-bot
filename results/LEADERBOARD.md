# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 3:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 701 windows, 19384 settled trades, 35 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 372 | 34.1 | 34.9 | $-244.03 | -6.6% | $755.97 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1631 | 50.2 | 49.4 | $-491.28 | -3.0% | $508.72 | -1.2 | done | can't tell from luck |
| value_ev10 | 899 | 38.4 | 39.1 | $-513.27 | -5.7% | $486.73 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 1991 | 51.6 | 50.8 | $-529.96 | -2.7% | $470.04 | -1.2 | done | can't tell from luck |
| value_ev5 | 1350 | 40.8 | 41.1 | $-608.49 | -4.5% | $391.51 | -1.4 | done | can't tell from luck |
| trend_filter | 1131 | 50.2 | 50.9 | $-634.55 | -5.6% | $365.45 | -1.9 | done | can't tell from luck |
| coinflip | 2796 | 50.2 | 50.3 | $-1193.62 | -4.3% | $-193.62 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1631 | 49.8 | 51.4 | $-1247.31 | -7.6% | $-247.31 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 1991 | 48.4 | 50.0 | $-1412.54 | -7.1% | $-412.54 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 2796 | 50.9 | 51.8 | $-1510.03 | -5.4% | $-510.03 | -3.0 | done | losing for real |
| always_up | 2796 | 47.3 | 49.5 | $-2405.83 | -8.6% | $-1405.83 | -4.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4394 | 48.2 | 49.1 | $-2569.51 |
| ETH | 4825 | 48.2 | 48.5 | $-2772.70 |
| SOL | 5057 | 48.2 | 48.6 | $-2942.31 |
| XRP | 5108 | 48.6 | 48.4 | $-2506.40 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
