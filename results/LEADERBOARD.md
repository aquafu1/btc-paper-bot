# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 9:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1206 windows, 33240 settled trades, 179 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 649 | 34.5 | 35.3 | $-438.79 | -6.8% | $561.21 | -1.3 | done | can't tell from luck |
| value_ev10 | 1589 | 38.6 | 39.2 | $-811.29 | -5.1% | $188.71 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3331 | 50.8 | 50.3 | $-1085.29 | -3.3% | $-85.29 | -1.9 | done | can't tell from luck |
| value_ev5 | 2401 | 40.4 | 41.1 | $-1260.09 | -5.2% | $-260.09 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2785 | 49.4 | 49.4 | $-1315.79 | -4.7% | $-315.79 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2785 | 50.6 | 51.1 | $-1636.00 | -5.9% | $-636.00 | -3.2 | done | losing for real |
| trend_filter | 1963 | 48.6 | 50.4 | $-1710.37 | -8.7% | $-710.37 | -4.0 | done | losing for real |
| momentum_15m_0.10pct | 3331 | 49.2 | 50.2 | $-2063.03 | -6.2% | $-1063.03 | -3.6 | done | losing for real |
| coinflip | 4802 | 50.0 | 50.1 | $-2182.07 | -4.5% | $-1182.07 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 4802 | 50.2 | 51.4 | $-2959.92 | -6.2% | $-1959.92 | -4.4 | done | losing for real |
| always_up | 4802 | 47.9 | 49.3 | $-3482.11 | -7.3% | $-2482.11 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7656 | 48.1 | 48.9 | $-4345.24 |
| ETH | 8274 | 48.0 | 48.3 | $-5015.27 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
