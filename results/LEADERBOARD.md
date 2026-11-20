# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 10:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 875 windows, 24145 settled trades, 60 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 454 | 35.5 | 34.9 | $-126.41 | -2.8% | $873.59 | -0.4 | done | can't tell from luck |
| value_ev10 | 1107 | 38.4 | 39.1 | $-581.80 | -5.3% | $418.20 | -1.4 | done | can't tell from luck |
| momentum_60m_0.30pct | 2040 | 50.0 | 49.8 | $-853.37 | -4.2% | $146.63 | -1.9 | done | can't tell from luck |
| value_ev5 | 1672 | 40.1 | 41.0 | $-949.02 | -5.7% | $50.98 | -2.0 | done | can't tell from luck |
| trend_filter | 1422 | 50.1 | 51.0 | $-964.82 | -6.8% | $35.18 | -2.6 | done | losing for real |
| reversal_15m_0.10pct | 2467 | 50.6 | 50.5 | $-971.51 | -3.9% | $28.49 | -2.0 | done | can't tell from luck |
| momentum_15m_0.10pct | 2467 | 49.4 | 50.4 | $-1394.59 | -5.7% | $-394.59 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 2040 | 50.0 | 51.0 | $-1401.12 | -6.9% | $-401.12 | -3.2 | done | losing for real |
| coinflip | 3492 | 50.1 | 50.3 | $-1561.87 | -4.5% | $-561.87 | -2.7 | done | losing for real |
| momentum_5m_0.00pct | 3492 | 51.2 | 51.8 | $-1651.56 | -4.7% | $-651.56 | -2.9 | done | losing for real |
| always_up | 3492 | 46.9 | 49.6 | $-3414.87 | -9.8% | $-2414.87 | -5.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5509 | 48.3 | 49.1 | $-2962.10 |
| ETH | 6004 | 48.1 | 48.5 | $-3834.27 |
| SOL | 6300 | 48.3 | 48.6 | $-3584.74 |
| XRP | 6332 | 48.4 | 48.5 | $-3489.83 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
