# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 3:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 606 windows, 16749 settled trades, 54 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1416 | 51.2 | 49.6 | $-197.18 | -1.4% | $802.82 | -0.5 | done | can't tell from luck |
| value_ev20 | 326 | 34.4 | 35.2 | $-234.70 | -7.2% | $765.30 | -1.0 | done | can't tell from luck |
| value_ev10 | 782 | 38.2 | 39.4 | $-547.21 | -7.0% | $452.79 | -1.6 | done | can't tell from luck |
| trend_filter | 966 | 50.2 | 51.0 | $-557.30 | -5.8% | $442.70 | -1.8 | done | can't tell from luck |
| value_ev5 | 1174 | 40.5 | 41.2 | $-687.73 | -5.9% | $312.27 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 1709 | 50.7 | 50.9 | $-799.16 | -4.7% | $200.84 | -2.0 | done | can't tell from luck |
| momentum_15m_0.10pct | 1709 | 49.3 | 50.0 | $-949.56 | -5.6% | $50.44 | -2.3 | done | losing for real |
| coinflip | 2417 | 50.0 | 50.5 | $-1208.74 | -5.0% | $-208.74 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1416 | 48.8 | 51.3 | $-1345.12 | -9.5% | $-345.12 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 2417 | 50.2 | 51.8 | $-1611.03 | -6.7% | $-611.03 | -3.4 | done | losing for real |
| always_up | 2417 | 47.0 | 49.8 | $-2327.41 | -9.6% | $-1327.41 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3817 | 48.0 | 49.2 | $-2521.15 |
| ETH | 4175 | 48.0 | 48.6 | $-2731.78 |
| SOL | 4350 | 47.9 | 48.7 | $-2945.50 |
| XRP | 4407 | 48.5 | 48.6 | $-2266.73 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
