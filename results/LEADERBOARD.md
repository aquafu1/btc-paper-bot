# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 2:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1035 windows, 28761 settled trades, 47 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 534 | 34.8 | 35.1 | $-264.76 | -5.0% | $735.24 | -0.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2926 | 51.2 | 50.5 | $-815.97 | -2.8% | $184.03 | -1.5 | done | can't tell from luck |
| value_ev10 | 1325 | 37.5 | 39.2 | $-976.31 | -7.4% | $23.69 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2464 | 49.8 | 49.6 | $-1112.65 | -4.5% | $-112.65 | -2.2 | done | losing for real |
| trend_filter | 1720 | 49.3 | 50.7 | $-1331.06 | -7.7% | $-331.06 | -3.3 | done | losing for real |
| value_ev5 | 2006 | 39.5 | 41.0 | $-1388.69 | -6.9% | $-388.69 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 2464 | 50.2 | 51.0 | $-1608.57 | -6.5% | $-608.57 | -3.3 | done | losing for real |
| coinflip | 4132 | 50.5 | 50.3 | $-1633.19 | -4.0% | $-633.19 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 2926 | 48.8 | 50.3 | $-2012.96 | -6.9% | $-1012.96 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 4132 | 50.7 | 51.5 | $-2298.40 | -5.6% | $-1298.40 | -3.7 | done | losing for real |
| always_up | 4132 | 47.4 | 49.5 | $-3543.77 | -8.6% | $-2543.77 | -5.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6559 | 48.3 | 49.1 | $-3639.79 |
| ETH | 7133 | 48.2 | 48.5 | $-4385.05 |
| SOL | 7509 | 48.2 | 48.6 | $-4275.07 |
| XRP | 7560 | 48.1 | 48.3 | $-4686.41 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
